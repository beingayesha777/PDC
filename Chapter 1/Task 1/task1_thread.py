import threading
import time


def print_hello():
  print("Hello, World!")


def run_threads(n):
  print(f"\nRunning with {n} threads...")
  start = time.time()

  threads = []
  for i in range(n):
    t = threading.Thread(target=print_hello)
    threads.append(t)
    t.start()

  for t in threads:
    t.join()

  end = time.time()
  print("Execution Time:", round(end - start, 6), "seconds")


# Run with 5, 10, 50 threads
run_threads(5)
run_threads(10)
run_threads(50)
