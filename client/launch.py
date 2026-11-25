import asyncio
import traceback
from argparse import Namespace

def normalize_args(args):
    if isinstance(args, Namespace):
        return args

    if isinstance(args, (tuple, list)):
        if len(args) == 1 and isinstance(args[0], Namespace):
            return args[0]

    return Namespace(
        connect=None,
        password=None,
        name=None
    )

def launch_edf5_client(*args):
    from .client import main
    args = normalize_args(args)
    asyncio.run(main(args))

    