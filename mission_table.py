# This file uses Ranger's armour

# Map Types
# ---
# base (inside)
# base (outside)
# housing complex
# industrial area
# suburbs
# treatment plant
# high rise (tracks)
# high rise (outpost)
# radio tower
# europe
# cave (narrow)
# cave (bridge)
# cave (water)
# mountains
# coast
# plain
# countryside

MISSION_TABLE = {
    1: {
        "name": "Today's Schedule",
         
        "w-normal":     0,
        "w-hard":       0,
        "w-hardest":    0,
        "w-inferno":    0,
        
        "a-normal":     0,
        "a-hard":       0,
        "a-hardest":    0,
        "a-inferno":    0,
        
        "map":          "base (inside)",
    },
    2: {
        "name": "Escape from Darkness",
          
        "w-normal":     2,
        "w-hard":       5,
        "w-hardest":    52,
        "w-inferno":    60,
        
        "a-normal":     424,
        "a-hard":       648,
        "a-hardest":    3080,
        "a-inferno":    5320,   
        
        "map":          "base (inside)",     
    },    
    3: {
        "name": "Crisis in Base 228: Part 1",
          
        "w-normal":     2,
        "w-hard":       5,
        "w-hardest":    52,
        "w-inferno":    60,
        
        "a-normal":     433,
        "a-hard":       669,
        "a-hardest":    3099,
        "a-inferno":    5389,
        
        "map":          "base (outside)",
    },
    4: {
        "name": "Crisis in Base 228: Part 2",
        
        "w-normal":     2,
        "w-hard":       5,
        "w-hardest":    52,
        "w-inferno":    61,
        
        "a-normal":     443,
        "a-hard":       692,
        "a-hardest":    3120,
        "a-inferno":    5459,        
        
        "map":          "base (outside)",
    },
    5: {
        "name": "Shattered Peace",
        
        "w-normal":     3,
        "w-hard":       6,
        "w-hardest":    53,
        "w-inferno":    61,
        
        "a-normal":     452,
        "a-hard":       713,
        "a-hardest":    3140,
        "a-inferno":    5529,
        
        "map":          "housing complex",
    },   
    6: {
        "name": "Unidentified Flying Objects",
        
        "w-normal":     3,
        "w-hard":       6,
        "w-hardest":    53,
        "w-inferno":    62,
        
        "a-normal":     462,
        "a-hard":       736,
        "a-hardest":    3161,
        "a-inferno":    5659,      
        
        "map":          "housing complex",  
    },
    7: {
        "name": "The Quiet Threat",
        
        "w-normal":     3,
        "w-hard":       7,
        "w-hardest":    53,
        "w-inferno":    62,
        
        "a-normal":     472,
        "a-hard":       758,
        "a-hardest":    3181,
        "a-inferno":    5668,       
        
        "map":          "industrial area",
    },     
    8: {
        "name": "Monsters Attack!",
        
        "w-normal":     3,
        "w-hard":       7,
        "w-hardest":    53,
        "w-inferno":    63,
        
        "a-normal":     481,
        "a-hard":       780,
        "a-hardest":    3201,
        "a-inferno":    5738,        
        
        "map":          "suburbs",
    },       
    9: {
        "name": "Wedge of Destruction",
        
        "w-normal":     4,
        "w-hard":       8,
        "w-hardest":    54,
        "w-inferno":    63,
        
        "a-normal":     491,
        "a-hard":       802,
        "a-hardest":    3222,
        "a-inferno":    5808,    
        
        "map":          "high rise (tracks)",    
    },   
    10: {
        "name": "Escape",
        
        "w-normal":     4,
        "w-hard":       8,
        "w-hardest":    54,
        "w-inferno":    64,
        
        "a-normal":     500,
        "a-hard":       824,
        "a-hardest":    3242,
        "a-inferno":    5878,
        "map":          "mountains",
    },   
    11: {
        "name": "Burning Sky",
        
        "w-normal":     4,
        "w-hard":       8,
        "w-hardest":    54,
        "w-inferno":    64,
        
        "a-normal":     510,
        "a-hard":       846,
        "a-hardest":    3263,
        "a-inferno":    5947,     
        
        "map":          "mountains",   
    },   
    12: {
        "name": "Spreading Disaster",
        
        "w-normal":     4,
        "w-hard":       9,
        "w-hardest":    54,
        "w-inferno":    65,
        
        "a-normal":     520,
        "a-hard":       868,
        "a-hardest":    3283,
        "a-inferno":    6017,        
        
        "map":          "treatment plant",
    },   
    13: {
        "name": "Turning Point",
        
        "w-normal":     5,
        "w-hard":       9,
        "w-hardest":    54,
        "w-inferno":    66,
        
        "a-normal":     529,
        "a-hard":       891,
        "a-hardest":    3304,
        "a-inferno":    6088,        
        
        "map":          "suburbs",
    }, 
    14: {
        "name": "Extermination",
        
        "w-normal":     5,
        "w-hard":       10,
        "w-hardest":    55,
        "w-inferno":    66,
        
        "a-normal":     539,
        "a-hard":       912,
        "a-hardest":    3323,
        "a-inferno":    6157,   
        
        "map":          "housing complex",     
    },     
    15: {
        "name": "Destroy the Giant Ship",
        
        "w-normal":     5,
        "w-hard":       10,
        "w-hardest":    55,
        "w-inferno":    67,
        
        "a-normal":     472,
        "a-hard":       758,
        "a-hardest":    3181,
        "a-inferno":    5668,        
        
        "map":          "europe",
    },   
    16: {
        "name": "Isolation",
        
        "w-normal":     5,
        "w-hard":       11,
        "w-hardest":    55,
        "w-inferno":    67,
        
        "a-normal":     558,
        "a-hard":       957,
        "a-hardest":    3364,
        "a-inferno":    6297,      
        
        "map":          "europe",  
    },   
    17: {
        "name": "Mastermind Revealed",
        
        "w-normal":     5,
        "w-hard":       11,
        "w-hardest":    55,
        "w-inferno":    68,
        
        "a-normal":     568,
        "a-hard":       979,
        "a-hardest":    3385,
        "a-inferno":    6367,        
        
        "map":          "treatment plant",
    },   
    18: {
        "name": "Secret of the Cave",
        
        "w-normal":     6,
        "w-hard":       11,
        "w-hardest":    56,
        "w-inferno":    68,
        
        "a-normal":     577,
        "a-hard":       1001,
        "a-hardest":    3405,
        "a-inferno":    6436,       
        
        "map":          "cave (narrow)", 
    },   
    19: {
        "name": "Eradication Plan",
        
        "w-normal":     6,
        "w-hard":       12,
        "w-hardest":    56,
        "w-inferno":    69,
        
        "a-normal":     587,
        "a-hard":       1023,
        "a-hardest":    3425,
        "a-inferno":    6506,    
        
        "map":          "high rise (tracks)",    
    },
    20: {
        "name": "Encounters on Return",
        
        "w-normal":     6,
        "w-hard":       12,
        "w-hardest":    56,
        "w-inferno":    69,
        
        "a-normal":     596,
        "a-hard":       1045,
        "a-hardest":    3446,
        "a-inferno":    6576,        
        
        "map":          "coast",
    },
    21: {
        "name": "Surprise Attack at Night",
        
        "w-normal":     6,
        "w-hard":       13,
        "w-hardest":    56,
        "w-inferno":    70,
        
        "a-normal":     606,
        "a-hard":       1067,
        "a-hardest":    3466,
        "a-inferno":    6646,       
        
        "map":          "industrial area", 
    },         
    22: {
        "name": "Scouting the Outpost",
        
        "w-normal":     7,
        "w-hard":       13,
        "w-hardest":    76,
        "w-inferno":    70,
        
        "a-normal":     616,
        "a-hard":       1089,
        "a-hardest":    3487,
        "a-inferno":    6715,        
        
        "map":          "high rise (outpost)",
    },  
    23: {
        "name": "Mountain of Wedges",
        
        "w-normal":     7,
        "w-hard":       14,
        "w-hardest":    57,
        "w-inferno":    71,
        
        "a-normal":     625,
        "a-hard":       1112,
        "a-hardest":    3507,
        "a-inferno":    6785,     
        
        "map":          "mountains",   
    },   
    24: {
        "name": "The Landing Ships",
        
        "w-normal":     7,
        "w-hard":       14,
        "w-hardest":    57,
        "w-inferno":    72,
        
        "a-normal":     635,
        "a-hard":       1134,
        "a-hardest":    3528,
        "a-inferno":    6856,     
        
        "map":          "treatment plant",   
    },    
    25: {
        "name": "Reinvasion",
        
        "w-normal":     7,
        "w-hard":       14,
        "w-hardest":    57,
        "w-inferno":    72,
        
        "a-normal":     644,
        "a-hard":       1256,
        "a-hardest":    3547,
        "a-inferno":    6925,        
        
        "map":          "radio tower",
    },   
    26: {
        "name": "Artillery Unit",
        
        "w-normal":     7,
        "w-hard":       15,
        "w-hardest":    57,
        "w-inferno":    73,
        
        "a-normal":     654,
        "a-hard":       1178,
        "a-hardest":    3568,
        "a-inferno":    6995,    
        
        "map":          "housing complex",    
    },   
    27: {
        "name": "Sniper Team",
        
        "w-normal":     8,
        "w-hard":       13,
        "w-hardest":    58,
        "w-inferno":    73,
        
        "a-normal":     664,
        "a-hard":       1200,
        "a-hardest":    3588,
        "a-inferno":    7065,      
        
        "map":          "treatment plant",  
    },
    28: {
        "name": "Red Drones",
        
        "w-normal":     8,
        "w-hard":       16,
        "w-hardest":    58,
        "w-inferno":    74,
        
        "a-normal":     673,
        "a-hard":       1222,
        "a-hardest":    3609,
        "a-inferno":    7135,    
        
        "map":          "high rise (tracks)",    
    },
    29: {
        "name": "Iron Wall",
        
        "w-normal":     8,
        "w-hard":       16,
        "w-hardest":    58,
        "w-inferno":    74,
        
        "a-normal":     683,
        "a-hard":       1244,
        "a-hardest":    3629,
        "a-inferno":    7204,    
        
        "map":          "radio tower",    
    },    
    30: {
        "name": "Destroy the Outpost: Plan A",
        
        "w-normal":     8,
        "w-hard":       17,
        "w-hardest":    58,
        "w-inferno":    75,
        
        "a-normal":     692,
        "a-hard":       1266,
        "a-hardest":    3659,
        "a-inferno":    7274,        
        
        "map":          "high rise (outpost)",
    },    
    31: {
        "name": "Destroy the Outpost: Plan B",
        
        "w-normal":     9,
        "w-hard":       17,
        "w-hardest":    59,
        "w-inferno":    75,
        
        "a-normal":     702,
        "a-hard":       1288,
        "a-hardest":    3670,
        "a-inferno":    7344,   
        
        "map":          "high rise (outpost)",     
    },
    32: {
        "name": "Cave Invasion Stage 1",
        
        "w-normal":     9,
        "w-hard":       17,
        "w-hardest":    59,
        "w-inferno":    76,
        
        "a-normal":     712,
        "a-hard":       1311,
        "a-hardest":    3690,
        "a-inferno":    7414,      
        
        "map":          "cave (narrow)",  
    },
    33: {
        "name": "Cave Invasion Stage 2",
        
        "w-normal":     9,
        "w-hard":       18,
        "w-hardest":    59,
        "w-inferno":    76,
        
        "a-normal":     721,
        "a-hard":       1332,
        "a-hardest":    3711,
        "a-inferno":    7483,
        
        "map":          "cave (bridge)",
    },
    34: {
        "name": "Cave Invasion Final Stage",
        
        "w-normal":     9,
        "w-hard":       18,
        "w-hardest":    59,
        "w-inferno":    77,
        
        "a-normal":     731,
        "a-hard":       1355,
        "a-hardest":    3731,
        "a-inferno":    7553,        
        
        "map":          "cave (water)",
    },
    35: {
        "name": "Berth",
        
        "w-normal":     10,
        "w-hard":       19,
        "w-hardest":    59,
        "w-inferno":    78,
        
        "a-normal":     740,
        "a-hard":       1377,
        "a-hardest":    3752,
        "a-inferno":    7624,   
        
        "map":          "coast",     
    },
    36: {
        "name": "Flying Killers",
        
        "w-normal":     10,
        "w-hard":       19,
        "w-hardest":    60,
        "w-inferno":    78,
        
        "a-normal":     750,
        "a-hard":       1399,
        "a-hardest":    3771,
        "a-inferno":    7693,   
        
        "map":          "housing complex",     
    },
    37: {
        "name": "Monster Elimination Plan",
        
        "w-normal":     10,
        "w-hard":       20,
        "w-hardest":    60,
        "w-inferno":    79,
        
        "a-normal":     760,
        "a-hard":       1421,
        "a-hardest":    3792,
        "a-inferno":    7763,       
        
        "map":          "treatment plant", 
    },
    38: {
        "name": "Plain of Conflict",
        
        "w-normal":     10,
        "w-hard":       20,
        "w-hardest":    60,
        "w-inferno":    79,
        
        "a-normal":     769,
        "a-hard":       1443,
        "a-hardest":    3812,
        "a-inferno":    7833, 
        
        "map":          "plain",
    },
    39: {
        "name": "Current Headquarters",
        
        "w-normal":     10,
        "w-hard":       20,
        "w-hardest":    60,
        "w-inferno":    80,
        
        "a-normal":     779,
        "a-hard":       1465,
        "a-hardest":    3833,
        "a-inferno":    7903,   
        
        "map":          "countryside",     
    },
    40: {
        "name": "Brutal Battlefield",
        
        "w-normal":     11,
        "w-hard":       21,
        "w-hardest":    61,
        "w-inferno":    80,
        
        "a-normal":     788,
        "a-hard":       1487,
        "a-hardest":    3853,
        "a-inferno":    7972,   
        
        "map":          "radio tower",     
    },
    41: {
        "name": "Assaulting the Outpost",
        
        "w-normal":     11,
        "w-hard":       21,
        "w-hardest":    61,
        "w-inferno":    81,
        
        "a-normal":     798,
        "a-hard":       1510,
        "a-hardest":    3873,
        "a-inferno":    8042,      
        
        "map":          "high rise (outpost)",  
    },
    42: {
        "name": "Saving Europe: Operation 1",
        
        "w-normal":     11,
        "w-hard":       22,
        "w-hardest":    61,
        "w-inferno":    81,
        
        "a-normal":     808,
        "a-hard":       1531,
        "a-hardest":    3894,
        "a-inferno":    8112,        
        
        "map":          "europe",
    },
    43: {
        "name": "Saving Europe: Operation 2",
        
        "w-normal":     11,
        "w-hard":       22,
        "w-hardest":    61,
        "w-inferno":    82,
        
        "a-normal":     817,
        "a-hard":       1554,
        "a-hardest":    3914,
        "a-inferno":    8182,       
        
        "map":          "europe", 
    },
    44: {
        "name": "Culling the FLying-Type",
        
        "w-normal":     12,
        "w-hard":       23,
        "w-hardest":    62,
        "w-inferno":    82,
        
        "a-normal":     827,
        "a-hard":       1576,
        "a-hardest":    3936,
        "a-inferno":    8251,        
        
        "map":          "suburbs",
    },
    45: {
        "name": "Brutal Battlefield",
        
        "w-normal":     12,
        "w-hard":       23,
        "w-hardest":    62,
        "w-inferno":    83,
        
        "a-normal":     836,
        "a-hard":       1598,
        "a-hardest":    3955,
        "a-inferno":    8321,  
        
        "map":          "radio tower",      
    },
    46: {
        "name": "Giant Ship Attack: 2nd Attempt",
        
        "w-normal":     12,
        "w-hard":       23,
        "w-hardest":    62,
        "w-inferno":    84,
        
        "a-normal":     846,
        "a-hard":       1620,
        "a-hardest":    3976,
        "a-inferno":    8392,        
        
        "map":          "treatment plant",
    },
    47: {
        "name": "Survivors",
        
        "w-normal":     12,
        "w-hard":       24,
        "w-hardest":    62,
        "w-inferno":    84,
        
        "a-normal":     856,
        "a-hard":       1642,
        "a-hardest":    3995,
        "a-inferno":    8461,      
        
        "map":          "treatment plant",  
    },
    48: {
        "name": "The Flying Saucers",
        
        "w-normal":     12,
        "w-hard":       24,
        "w-hardest":    62,
        "w-inferno":    85,
        
        "a-normal":     865,
        "a-hard":       1664,
        "a-hardest":    4016,
        "a-inferno":    8531,     
        
        "map":          "radio tower",   
    },
    49: {
        "name": "Airborne Fighters: Part 1",
        
        "w-normal":     13,
        "w-hard":       25,
        "w-hardest":    63,
        "w-inferno":    85,
        
        "a-normal":     875,
        "a-hard":       1686,
        "a-hardest":    4036,
        "a-inferno":    8601,     
        
        "map":          "housing complex",   
    },
    50: {
        "name": "Airborne Fighters: Part 2",
        
        "w-normal":     13,
        "w-hard":       25,
        "w-hardest":    63,
        "w-inferno":    86,
        
        "a-normal":     884,
        "a-hard":       1709,
        "a-hardest":    4057,
        "a-inferno":    8671,
        
        "map":          "treatment plant",
    },
    51: {
        "name": "Attacking the Fleet",
        
        "w-normal":     13,
        "w-hard":       26,
        "w-hardest":    63,
        "w-inferno":    86,
        
        "a-normal":     894,
        "a-hard":       1730,
        "a-hardest":    4077,
        "a-inferno":    8740,    
        
        "map":          "industrial area",    
    },
    52: {
        "name": "Underground Trap",
        
        "w-normal":     13,
        "w-hard":       26,
        "w-hardest":    63,
        "w-inferno":    87,
        
        "a-normal":     904,
        "a-hard":       1753,
        "a-hardest":    4097,
        "a-inferno":    8810,      
        
        "map":          "cave (narrow)",  
    },
    53: {
        "name": "The Army Group Raid",
        
        "w-normal":     14,
        "w-hard":       27,
        "w-hardest":    64,
        "w-inferno":    87,
        
        "a-normal":     913,
        "a-hard":       1775,
        "a-hardest":    4118,
        "a-inferno":    8880,    
        
        "map":          "radio tower",    
    },
    54: {
        "name": "Wire-puller",
        
        "w-normal":     14,
        "w-hard":       27,
        "w-hardest":    64,
        "w-inferno":    88,
        
        "a-normal":     923,
        "a-hard":       1797,
        "a-hardest":    4138,
        "a-inferno":    8950,    
        
        "map":          "high rise (tracks)",    
    },
    55: {
        "name": "Hiding Behind the Web",
        
        "w-normal":     14,
        "w-hard":       27,
        "w-hardest":    64,
        "w-inferno":    88,
        
        "a-normal":     932,
        "a-hard":       1819,
        "a-hardest":    4159,
        "a-inferno":    9019,   
        
        "map":          "high rise (tracks)",     
    },
    56: {
        "name": "Predators on Thread",
        
        "w-normal":     14,
        "w-hard":       28,
        "w-hardest":    64,
        "w-inferno":    89,
        
        "a-normal":     942,
        "a-hard":       1841,
        "a-hardest":    4179,
        "a-inferno":    9089,     
        
        "map":          "radio tower",   
    },
    57: {
        "name": "Scuffle in the City",
        
        "w-normal":     15,
        "w-hard":       28,
        "w-hardest":    65,
        "w-inferno":    90,
        
        "a-normal":     952,
        "a-hard":       1864,
        "a-hardest":    4200,
        "a-inferno":    9160,       
        
        "map":          "europe", 
    },
    58: {
        "name": "Hidden Threat",
        
        "w-normal":     15,
        "w-hard":       29,
        "w-hardest":    65,
        "w-inferno":    90,
        
        "a-normal":     961,
        "a-hard":       1885,
        "a-hardest":    4219,
        "a-inferno":    9229,        
        
        "map":          "treatment plant",
    },
    59: {
        "name": "Break the Barrier",
        
        "w-normal":     15,
        "w-hard":       29,
        "w-hardest":    65,
        "w-inferno":    91,
        
        "a-normal":     971,
        "a-hard":       1908,
        "a-hardest":    4240,
        "a-inferno":    9299,     
        
        "map":          "high rise (tracks)",   
    },
    60: {
        "name": "Mountain Investigation",
        
        "w-normal":     15,
        "w-hard":       30,
        "w-hardest":    65,
        "w-inferno":    91,
        
        "a-normal":     980,
        "a-hard":       1929,
        "a-hardest":    4260,
        "a-inferno":    9369,   
        
        "map":          "mountains",    
    },
    61: {
        "name": "Destroy Large Flying Saucers",
        
        "w-normal":     15,
        "w-hard":       30,
        "w-hardest":    65,
        "w-inferno":    92,
        
        "a-normal":     990,
        "a-hard":       1952,
        "a-hardest":    4281,
        "a-inferno":    9439, 
        
        "map":          "mountains",       
    },
    62: {
        "name": "Sweeping Monster Balls",
        
        "w-normal":     16,
        "w-hard":       30,
        "w-hardest":    66,
        "w-inferno":    92,
        
        "a-normal":     1000,
        "a-hard":       1974,
        "a-hardest":    4301,
        "a-inferno":    9508,       
        
        "map":          "treatment plant", 
    },
    63: {
        "name": "Recapturing the Industrial Area",
        
        "w-normal":     16,
        "w-hard":       31,
        "w-hardest":    66,
        "w-inferno":    93,
        
        "a-normal":     1009,
        "a-hard":       1996,
        "a-hardest":    4321,
        "a-inferno":    9578,        
        
        "map":          "industrial area",
    },
    64: {
        "name": "Winged Legion",
        
        "w-normal":     16,
        "w-hard":       31,
        "w-hardest":    66,
        "w-inferno":    93,
        
        "a-normal":     1019,
        "a-hard":       2018,
        "a-hardest":    4342,
        "a-inferno":    9648,        
    },
    65: {
        "name": "Landing Giant Ship",
        
        "w-normal":     16,
        "w-hard":       32,
        "w-hardest":    66,
        "w-inferno":    94,
        
        "a-normal":     1028,
        "a-hard":       2040,
        "a-hardest":    4362,
        "a-inferno":    9718,      
        
        "map":          "housing complex",  
    },
    66: {
        "name": "Falling Monster Balls",
        
        "w-normal":     17,
        "w-hard":       32,
        "w-hardest":    67,
        "w-inferno":    94,
        
        "a-normal":     1038,
        "a-hard":       2062,
        "a-hardest":    4383,
        "a-inferno":    9787,   
        
        "map":          "housing complex",     
    },
    67: {
        "name": "Extraterrestrial Riders",
        
        "w-normal":     17,
        "w-hard":       33,
        "w-hardest":    67,
        "w-inferno":    95,
        
        "a-normal":     1048,
        "a-hard":       2084,
        "a-hardest":    4403,
        "a-inferno":    9857,     
        
        "map":          "high rise (tracks)",   
    },
    68: {
        "name": "Crashing Giant Pylons",
        
        "w-normal":     17,
        "w-hard":       33,
        "w-hardest":    67,
        "w-inferno":    96,
        
        "a-normal":     1057,
        "a-hard":       2107,
        "a-hardest":    4424,
        "a-inferno":    9928,        
        
        "map":          "radio tower",
    },
    69: {
        "name": "Enormous Mutants",
        
        "w-normal":     17,
        "w-hard":       33,
        "w-hardest":    67,
        "w-inferno":    96,
        
        "a-normal":     1067,
        "a-hard":       2128,
        "a-hardest":    4443,
        "a-inferno":    9997,       
        
        "map":          "housing complex", 
    },
    70: {
        "name": "Aircrafts",
        
        "w-normal":     17,
        "w-hard":       34,
        "w-hardest":    67,
        "w-inferno":    97,
        
        "a-normal":     1076,
        "a-hard":       2151,
        "a-hardest":    4464,
        "a-inferno":    10067,    
        
        "map":          "treatment plant",    
    },
    71: {
        "name": "Anchors Destruction Plan",
        
        "w-normal":     18,
        "w-hard":       34,
        "w-hardest":    68,
        "w-inferno":    97,
        
        "a-normal":     1086,
        "a-hard":       2173,
        "a-hardest":    4484,
        "a-inferno":    10137,    
        
        "map":          "radio tower",    
    },
    72: {
        "name": "Battle in the Fog",
        
        "w-normal":     18,
        "w-hard":       35,
        "w-hardest":    68,
        "w-inferno":    98,
        
        "a-normal":     1096,
        "a-hard":       2195,
        "a-hardest":    4505,
        "a-inferno":    10207,     
        
        "map":          "radio tower",   
    },
    73: {
        "name": "Light Defenses",
        
        "w-normal":     18,
        "w-hard":       35,
        "w-hardest":    68,
        "w-inferno":    98,
        
        "a-normal":     1105,
        "a-hard":       2217,
        "a-hardest":    4525,
        "a-inferno":    10276,     
        
        "map":          "industrial area",   
    },
    74: {
        "name": "Flying Unit",
        
        "w-normal":     18,
        "w-hard":       36,
        "w-hardest":    68,
        "w-inferno":    99,
        
        "a-normal":     1115,
        "a-hard":       2239,
        "a-hardest":    4545,
        "a-inferno":    10346,     
        
        "map":          "europe",   
    },
    75: {
        "name": "Fighters Ambush",
        
        "w-normal":     19,
        "w-hard":       36,
        "w-hardest":    69,
        "w-inferno":    99,
        
        "a-normal":     1124,
        "a-hard":       2261,
        "a-hardest":    4566,
        "a-inferno":    10416,        
        
        "map":          "suburbs",
    },
    76: {
        "name": "Sieged City",
        
        "w-normal":     19,
        "w-hard":       36,
        "w-hardest":    69,
        "w-inferno":    99,
        
        "a-normal":     1134,
        "a-hard":       2283,
        "a-hardest":    4586,
        "a-inferno":    10486,      
        
        "map":          "housing complex",  
    },
    77: {
        "name": "Doomed Queens",
        
        "w-normal":     19,
        "w-hard":       37,
        "w-hardest":    69,
        "w-inferno":    99,
        
        "a-normal":     1144,
        "a-hard":       2305,
        "a-hardest":    4607,
        "a-inferno":    10555,      
        
        "map":          "coast",  
    },
    78: {
        "name": "Monster Extermination",
        
        "w-normal":     19,
        "w-hard":       37,
        "w-hardest":    69,
        "w-inferno":    99,
        
        "a-normal":     1153,
        "a-hard":       2328,
        "a-hardest":    4627,
        "a-inferno":    10625,    
        
        "map":          "suburbs",    
    },
    79: {
        "name": "Reclaiming Base 228: Stage 1",
        
        "w-normal":     20,
        "w-hard":       38,
        "w-hardest":    70,
        "w-inferno":    99,
        
        "a-normal":     1163,
        "a-hard":       2350,
        "a-hardest":    4648,
        "a-inferno":    10696,   
        
        "map":          "mountains",     
    },
    80: {
        "name": "Reclaiming Base 228: Stage 2",
        
        "w-normal":     20,
        "w-hard":       38,
        "w-hardest":    70,
        "w-inferno":    99,
        
        "a-normal":     1172,
        "a-hard":       2372,
        "a-hardest":    4667,
        "a-inferno":    10765,
        
        "map":          "base (outside)",        
    },
    81: {
        "name": "Reclaiming Base 228: Stage 3",
        
        "w-normal":     20,
        "w-hard":       39,
        "w-hardest":    70,
        "w-inferno":    99,
        
        "a-normal":     1182,
        "a-hard":       2394,
        "a-hardest":    4688,
        "a-inferno":    10835,       
        
        "map":          "base (inside)", 
    },
    82: {
        "name": "Reclaiming Base 228: Retreat",
        
        "w-normal":     20,
        "w-hard":       39,
        "w-hardest":    70,
        "w-inferno":    99,
        
        "a-normal":     1192,
        "a-hard":       2416,
        "a-hardest":    4708,
        "a-inferno":    10905,      
        
        "map":          "base (outside)",  
    },
    83: {
        "name": "Defeat Archelus",
        
        "w-normal":     20,
        "w-hard":       39,
        "w-hardest":    70,
        "w-inferno":    99,
        
        "a-normal":     1201,
        "a-hard":       2438,
        "a-hardest":    4729,
        "a-inferno":    10975,     
        
        "map":          "industrial area",   
    },
    84: {
        "name": "City of Giant Pylons",
        
        "w-normal":     21,
        "w-hard":       40,
        "w-hardest":    71,
        "w-inferno":    99,
        
        "a-normal":     1211,
        "a-hard":       2460,
        "a-hardest":    4749,
        "a-inferno":    11044, 
        
        "map":          "treatment plant",       
    },
    85: {
        "name": "Incoming Larvae",
        
        "w-normal":     21,
        "w-hard":       40,
        "w-hardest":    71,
        "w-inferno":    99,
        
        "a-normal":     1220,
        "a-hard":       2482,
        "a-hardest":    4769,
        "a-inferno":    11114,  
        
        "map":          "treatment plant",      
    },
    86: {
        "name": "Secret in the Dark",
        
        "w-normal":     21,
        "w-hard":       41,
        "w-hardest":    71,
        "w-inferno":    99,
        
        "a-normal":     1230,
        "a-hard":       2504,
        "a-hardest":    4790,
        "a-inferno":    11184,       
        
        "map":          "cave (bridge)", 
    },
    87: {
        "name": "Approaching Monster Balls",
        
        "w-normal":     21,
        "w-hard":       41,
        "w-hardest":    71,
        "w-inferno":    99,
        
        "a-normal":     1240,
        "a-hard":       2527,
        "a-hardest":    4810,
        "a-inferno":    11254,     
        
        "map":          "coast",   
    },
    88: {
        "name": "Threads Everywhere",
        
        "w-normal":     22,
        "w-hard":       42,
        "w-hardest":    72,
        "w-inferno":    99,
        
        "a-normal":     1249,
        "a-hard":       2548,
        "a-hardest":    4831,
        "a-inferno":    11323,    
        
        "map":          "treatment plant",    
    },
    89: {
        "name": "Flying-type Extermination",
        
        "w-normal":     22,
        "w-hard":       42,
        "w-hardest":    72,
        "w-inferno":    99,
        
        "a-normal":     1259,
        "a-hard":       2571,
        "a-hardest":    4851,
        "a-inferno":    11393,    
        
        "map":          "mountains",
    },
    90: {
        "name": "Broken Land",
        
        "w-normal":     22,
        "w-hard":       42,
        "w-hardest":    72,
        "w-inferno":    99,
        
        "a-normal":     1268,
        "a-hard":       2593,
        "a-hardest":    4872,
        "a-inferno":    11464,     
        
        "map":          "radio tower",   
    },
    91: {
        "name": "Sparkling Abyss",
        
        "w-normal":     22,
        "w-hard":       43,
        "w-hardest":    72,
        "w-inferno":    99,
        
        "a-normal":     1278,
        "a-hard":       2615,
        "a-hardest":    4891,
        "a-inferno":    11533,      
        
        "map":          "cave (bridge)",  
    },
    92: {
        "name": "Attack of the Flying Fleet",
        
        "w-normal":     22,
        "w-hard":       43,
        "w-hardest":    72,
        "w-inferno":    99,
        
        "a-normal":     1288,
        "a-hard":       2637,
        "a-hardest":    4912,
        "a-inferno":    11603,   
        
        "map":          "high rise (tracks)",     
    },
    93: {
        "name": "Mountain Traps",
        
        "w-normal":     23,
        "w-hard":       44,
        "w-hardest":    73,
        "w-inferno":    99,
        
        "a-normal":     1297,
        "a-hard":       2659,
        "a-hardest":    4932,
        "a-inferno":    11673,   
        
        "map":          "mountains",    
    },
    94: {
        "name": "Bloody Battle",
        
        "w-normal":     23,
        "w-hard":       44,
        "w-hardest":    73,
        "w-inferno":    99,
        
        "a-normal":     1307,
        "a-hard":       2681,
        "a-hardest":    4953,
        "a-inferno":    11743,    
        
        "map":          "high rise (tracks)",    
    },
    95: {
        "name": "Drop Location",
        
        "w-normal":     23,
        "w-hard":       45,
        "w-hardest":    73,
        "w-inferno":    99,
        
        "a-normal":     1316,
        "a-hard":       2703,
        "a-hardest":    4973,
        "a-inferno":    11812,     
        
        "map":          "mountains",   
    },
    96: {
        "name": "Land of Monsters",
        
        "w-normal":     23,
        "w-hard":       45,
        "w-hardest":    73,
        "w-inferno":    99,
        
        "a-normal":     1326,
        "a-hard":       2726,
        "a-hardest":    4993,
        "a-inferno":    11882,        
        
        "map":          "industrial area",
    },
    97: {
        "name": "Steel Covered by Threads",
        
        "w-normal":     24,
        "w-hard":       46,
        "w-hardest":    74,
        "w-inferno":    99,
        
        "a-normal":     1336,
        "a-hard":       2747,
        "a-hardest":    5014,
        "a-inferno":    11952,        
        
        "map":          "radio tower",
    },
    98: {
        "name": "Coastal Defense Line",
        
        "w-normal":     24,
        "w-hard":       46,
        "w-hardest":    74,
        "w-inferno":    99,
        
        "a-normal":     1345,
        "a-hard":       2770,
        "a-hardest":    5034,
        "a-inferno":    12022,      
        
        "map":          "coast",  
    },
    99: {
        "name": "Intense Battle Underground",
        
        "w-normal":     24,
        "w-hard":       46,
        "w-hardest":    74,
        "w-inferno":    99,
        
        "a-normal":     1355,
        "a-hard":       2792,
        "a-hardest":    5055,
        "a-inferno":    12091,   
        
        "map":          "cave (narrow)",     
    },
    100: {
        "name": "Greatest Final Confrontation",
        
        "w-normal":     24,
        "w-hard":       47,
        "w-hardest":    74,
        "w-inferno":    99,
        
        "a-normal":     1364,
        "a-hard":       2814,
        "a-hardest":    5075,
        "a-inferno":    12161,   
        
        "map":          "plain",     
    },
    101: {
        "name": "Crumbling City",
        
        "w-normal":     25,
        "w-hard":       47,
        "w-hardest":    75,
        "w-inferno":    99,
        
        "a-normal":     1374,
        "a-hard":       2836,
        "a-hardest":    5096,
        "a-inferno":    12232,    
        
        "map":          "high rise (tracks)",    
    },
    102: {
        "name": "Forced Entry",
        
        "w-normal":     25,
        "w-hard":       48,
        "w-hardest":    75,
        "w-inferno":    99,
        
        "a-normal":     1384,
        "a-hard":       2858,
        "a-hardest":    5115,
        "a-inferno":    12301,    
        
        "map":          "coast",    
    },
    103: {
        "name": "Tornado",
        
        "w-normal":     25,
        "w-hard":       48,
        "w-hardest":    75,
        "w-inferno":    99,
        
        "a-normal":     1393,
        "a-hard":       2880,
        "a-hardest":    5136,
        "a-inferno":    12371,    
        
        "map":          "mountains",    
    },
    104: {
        "name": "Against All Odds",
        
        "w-normal":     25,
        "w-hard":       49,
        "w-hardest":    75,
        "w-inferno":    99,
        
        "a-normal":     1403,
        "a-hard":       2902,
        "a-hardest":    5156,
        "a-inferno":    12441, 
        
        "map":          "high rise (tracks)",       
    },
    105: {
        "name": "Monster Banquet",
        
        "w-normal":     25,
        "w-hard":       49,
        "w-hardest":    75,
        "w-inferno":    99,
        
        "a-normal":     1412,
        "a-hard":       2925,
        "a-hardest":    5177,
        "a-inferno":    12511,     
        
        "map":          "radio tower",   
    },
    106: {
        "name": "Suicide Squad",
        
        "w-normal":     26,
        "w-hard":       49,
        "w-hardest":    76,
        "w-inferno":    99,
        
        "a-normal":     1422,
        "a-hard":       2946,
        "a-hardest":    5197,
        "a-inferno":    12580,    
        
        "map":          "treatment plant",    
    },
    107: {
        "name": "Invader Assembly",
        
        "w-normal":     26,
        "w-hard":       50,
        "w-hardest":    76,
        "w-inferno":    99,
        
        "a-normal":     1432,
        "a-hard":       2969,
        "a-hardest":    5217,
        "a-inferno":    12650,     
        
        "map":          "high rise (tracks)",   
    },
    108: {
        "name": "Scorched Earth",
        
        "w-normal":     26,
        "w-hard":       50,
        "w-hardest":    76,
        "w-inferno":    99,
        
        "a-normal":     1441,
        "a-hard":       2991,
        "a-hardest":    5328,
        "a-inferno":    12720,   
        
        "map":          "treatment plant",     
    },
    109: {
        "name": "No. 11",
        
        "w-normal":     27,
        "w-hard":       52,
        "w-hardest":    77,
        "w-inferno":    99,
        
        "a-normal":     1470,
        "a-hard":       3057,
        "a-hardest":    5299,
        "a-inferno":    12929,    
        
        "map":          "suburbs",    
    },
    110: {
        "name": "The Nameless",
        
        "w-normal":     27,
        "w-hard":       52,
        "w-hardest":    77,
        "w-inferno":    99,
        
        "a-normal":     1480,
        "a-hard":       3080,
        "a-hardest":    5320,
        "a-inferno":    13000,       
        
        "map":          "high rise (tracks)", 
    },
}