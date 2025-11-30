import asyncio
import time
import random

# Define a maximum number of cycles to run before stopping the loop deterministically.
MAX_CYCLES = 3

def print_hello(loop, current_cycle):
    """
    Prints 'Hello' and schedules the next step ('World').
    This function is synchronous and runs entirely on the event loop thread.
    """
    print (f"[{current_cycle}/{MAX_CYCLES}] Hello")

  
    if current_cycle < MAX_CYCLES:
        # Schedule print_world to run 1 second from now
        loop.call_later(1, print_world, loop, current_cycle)
    else:
        # Stop the loop if we've reached the maximum cycles
        loop.stop()

def print_world(loop, current_cycle):
    """
    Prints 'World' and schedules the previous step ('Hello') to create a cycle.
    """
    print (f"[{current_cycle}/{MAX_CYCLES}] World!")

    # If we haven't reached the end, schedule the next cycle's 'Hello'.
    if current_cycle < MAX_CYCLES:
        # Schedule the next 'Hello' to run 1 second from now, and increment the counter
        loop.call_later(1, print_hello, loop, current_cycle + 1)
    else:
        # Stop the loop if we've reached the maximum cycles (this will only happen if MAX_CYCLES is 1)
        loop.stop()


if __name__ == '__main__':
    print(f"Event Loop Callback simulation running for {MAX_CYCLES} cycles.")
    loop = asyncio.get_event_loop()

    
    loop.call_soon(print_hello, loop, 1)

    # Run the loop forever, until loop.stop() is explicitly called by our functions
    loop.run_forever()
    
    # Clean up the loop
    loop.close()