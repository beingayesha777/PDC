# Using a Process Pool – Example: Printing "Hello, World!"
import multiprocessing

def say_hello(data):
    """Each process prints 'Hello, World!' along with its input."""
    print(f"Process handling {data}: Hello, World!")
    return f"Hello, World! from {data}"

if __name__ == '__main__':
    inputs = list(range(4))  # 4 tasks for demonstration
    pool = multiprocessing.Pool(processes=4)

    # Each worker in the pool runs say_hello()
    pool_outputs = pool.map(say_hello, inputs)

    pool.close()
    pool.join()

    print('\nPool Output:', pool_outputs)
