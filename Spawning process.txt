# Spawn a Process – Example: Printing "Hello, World!" using multiprocessing
import multiprocessing

def say_hello(i):
    print('Process number %s says: Hello, World!' % i)

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=say_hello, args=(i,))
        process.start()
        process.join()
