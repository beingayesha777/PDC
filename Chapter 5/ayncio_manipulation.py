import asyncio

@asyncio.coroutine
def hello_coroutine():
    """Prints 'Hello' concurrently."""
    print('Asyncio.Task: Starting Hello...')
    # Use yield from asyncio.sleep(1) to pause and allow the event loop to switch to other tasks
    yield from asyncio.sleep(1)
    print('Asyncio.Task: Completed Hello')
    return 'Hello'

@asyncio.coroutine
def world_coroutine():
    """Prints 'World' concurrently."""
    print('Asyncio.Task: Starting World...')
    yield from asyncio.sleep(1)
    print('Asyncio.Task: Completed World')
    return 'World'

@asyncio.coroutine
def exclamation_coroutine():
    """Prints '!' concurrently."""
    print('Asyncio.Task: Starting Exclamation...')
    yield from asyncio.sleep(1)
    print('Asyncio.Task: Completed !')
    return '!'


if __name__ == '__main__':
    print('Asyncio using Asyncio.Task to print "Hello World!" in parallel')
    
    # 1. Explicitly create asyncio.Task objects for each coroutine, just like the original example.
    task_list = [asyncio.Task(hello_coroutine()),
                 asyncio.Task(world_coroutine()),
                 asyncio.Task(exclamation_coroutine())]
                 
    # 2. Get the event loop
    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(asyncio.wait(task_list))
    
    # 4. Clean up
    loop.close()