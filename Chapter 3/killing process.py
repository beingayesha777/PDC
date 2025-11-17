import multiprocessing
import time

def say_hello():
    print("Starting function")
    print("Hello, World!")
    time.sleep(2)  # Simulate some work
    print("Finished function")

if __name__ == '__main__':
    p = multiprocessing.Process(target=say_hello)
    print('Process before execution:', p, p.is_alive())

    p.start()
    print('Process running:', p, p.is_alive())

    # Kill (terminate) the process before it naturally finishes
    p.terminate()
    print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())

    print('Process exit code:', p.exitcode)
