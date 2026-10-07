"""Run a script at below-normal CPU priority (Windows), so a post-hoc job uses the slack of a machine the open searches keep busy.

    python -u _reference/data/low_priority.py <script.py> [args...]

The priority class is inherited by the child processes the script starts (a multiprocessing pool, the simulator's bench).
"""
import ctypes
import runpy
import sys

if __name__ == "__main__":
    if sys.platform == "win32":
        k32 = ctypes.windll.kernel32
        k32.GetCurrentProcess.restype = ctypes.c_void_p   # a HANDLE is pointer-sized: without this the pseudo-handle -1 is truncated
        k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        k32.SetPriorityClass.restype = ctypes.c_int
        if not k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000):   # BELOW_NORMAL_PRIORITY_CLASS
            print(f"low_priority: SetPriorityClass failed (error {k32.GetLastError()})", flush=True)
    target = sys.argv[1]
    sys.argv = sys.argv[1:]
    runpy.run_path(target, run_name="__main__")
