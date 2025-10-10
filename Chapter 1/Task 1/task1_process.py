import multiprocessing
import time


def print_hello():
  print("Hello, World!")


def run_processes(n):
  print(f"\nRunning with {n} processes...")
  start = time.time()

  processes = []
  for i in range(n):
    p = multiprocessing.Process(target=print_hello)
    processes.append(p)
    p.start()

  for p in processes:
    p.join()

  end = time.time()
  print("Execution Time:", round(end - start, 6), "seconds")


# Run with 5, 10, 50 processes
if __name__ == "__main__":
  run_processes(5)
  run_processes(10)
  run_processes(50)
