"""An exclusive lock on a file, on Linux (fcntl, the cloud sessions) and on Windows (msvcrt, the local machine) alike.

    from filelock import locked
    with locked(path.with_suffix(".lock")):
        ...   # read, merge and write a record other processes also write

Scripts that run one class per process and merge into one record take it (2026-10-01: the derive_* scripts imported fcntl, which does
not exist on Windows, so they failed there).
"""
import contextlib
import sys
import time


@contextlib.contextmanager
def locked(path):
    fh = open(path, "a+")
    try:
        if sys.platform.startswith("win"):
            import msvcrt
            fh.seek(0)
            while True:
                try:
                    msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:   # held by another process: wait and try again
                    time.sleep(0.05)
        else:
            import fcntl
            fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            if sys.platform.startswith("win"):
                import msvcrt
                fh.seek(0)
                try:
                    msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)
                except OSError:
                    pass
            else:
                import fcntl
                fcntl.flock(fh, fcntl.LOCK_UN)
    finally:
        fh.close()
