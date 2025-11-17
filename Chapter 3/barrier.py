# Barrier Example – Printing "Hello, World!" with and without synchronization
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def hello_with_barrier(synchronizer, serializer):
    """Each process waits at the barrier before printing."""
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait until all barrier participants reach this point
    with serializer:
        print(f"{name} says: Hello, World!")

def hello_without_barrier():
    """Each process prints independently (no synchronization)."""
    name = multiprocessing.current_process().name
    print(f"{name} says: Hello, World!")

if __name__ == '__main__':
    synchronizer = Barrier(2)  # Barrier for 2 processes
    serializer = Lock()        # Prevents mixed print output

    # Processes using barrier
    Process(name='p1 - hello_with_barrier',
            target=hello_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p2 - hello_with_barrier',
            target=hello_with_barrier,
            args=(synchronizer, serializer)).start()

    # Processes without barrier
    Process(name='p3 - hello_without_barrier',
            target=hello_without_barrier).start()
    Process(name='p4 - hello_without_barrier',
            target=hello_without_barrier).start()


