import pymem
import psutil
import ctypes
from ctypes import wintypes

from .offsets import RANGER_ARMOR

class EDF5Memory:
    
    def __init__(self):
        self.pm = None
        
    # Finds EDF5 in processes
    def find_edf5(self):
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                if proc.info["name"] == "EDF5.exe":
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
            
        return None    
    
    def connect(self):
        self.pm = pymem.Pymem("EDF5.exe")
        
    def disconnect(self):
        self.pm = None
        
    def is_connected(self):
        return self.pm is not None
    
    def get_module_base(self):
        return self.pm.process_base.lpBaseOfDll
    
    # Renamed from get_armor_base
    def get_player_data_base(self):
        module_base = self.get_module_base()
        r10 = self.pm.read_ulonglong(module_base + 0x125AB30)
        return r10    
    
    # Check the game is in a safe state to modify memory, before doing so
    # We achieve this by checking where we last knew where RANGER_ARMOR is, and is a value that could realistically be the value of Ranger's armor        
    def is_safe_to_write(self):
        try:
            base = self.get_player_data_base()
            value = self.read_i32(base + RANGER_ARMOR)                    
            return value >= 0 and value < 999999999
        except Exception:
            return False    
        
    # Ask windows for some memory inside of EDF5, as close to the target 'address' as possible. This is used for 'hacking' the mission menu for our needs
    def allocate_near(self, address, size=0x1000):
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.VirtualAllocEx.restype = ctypes.c_void_p
        kernel32.VirtualAllocEx.argtypes = [wintypes.HANDLE, ctypes.c_void_p, ctypes.c_size_t, wintypes.DWORD, wintypes.DWORD]
        
        step = 0x10000 # Windows hands out memory in 64kb blocks
        start = address & ~(step - 1)
        
        # Look for a space just below and just above the target address, then a bit further out each time it's unsuccessful
        for distance in range(step, 0x70000000, step):
            for candidate in (start - distance, start + distance):
                result = kernel32.VirtualAllocEx(self.pm.process_handle, candidate, size, 0x3000, 0x40)
                if result:
                    return result
                
        return None
        
    # Reading and writing functions, for bytes, addresses, floats etc.
    
    def read_u8(self, address):
        return self.pm.read_uchar(address)
    
    def write_u8(self, address, value):
        self.pm.write_uchar(address, value)
    
    def read_i32(self, address):
        return self.pm.read_int(address)
    
    def write_i32(self, address, value):
        self.pm.write_int(address, value)    
    
    def read_bytes(self, address, length):
        return self.pm.read_bytes(address, length)
    
    def write_bytes(self, address, value):
        self.pm.write_bytes(address, value, len(value))
        
    def read_u64(self, address):
        return self.pm.read_ulonglong(address)
    
    def write_u64(self, address, value):
        return self.pm.write_ulonglong(address, value)
    
    def read_utf16(self, address, size=34):
        data = self.read_bytes(address, size)
        return data.decode("utf-16-le").split("\x00", 1)[0]