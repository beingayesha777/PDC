import asyncio
import sys

# @asyncio.coroutine is a decorator used in older Python versions (pre-3.5/3.8 style).
# It marks a generator-based coroutine.
@asyncio.coroutine
def say_hello(future):
    # Simulate work with a sleep, using 'yield from' instead of 'await'
    yield from asyncio.sleep(1)
    # Set the result string into the future object
    future.set_result('Hello')

@asyncio.coroutine
def say_world(future):
    yield from asyncio.sleep(1)
    future.set_result('World')

def got_result(future):
    # This callback prints the result once the future is done
    print(future.result())

if __name__ == '__main__':
    # Get the standard event loop
    loop = asyncio.get_event_loop()
    
    # Create manual Future objects to hold our results
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Schedule the coroutines, passing the futures into them
    tasks = [say_hello(future1),
             say_world(future2)]

    # Attach the callback function to be called when tasks finish
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Run the loop until all tasks in the list are complete
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()