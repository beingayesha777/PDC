import asyncio
import sys

# Coroutines are used here to simulate a deterministic sequence of "states"
# to print "Hello World!".

@asyncio.coroutine
def start_coroutine():
    """Initial state: prints 'Hello' and transitions to the next state."""
    print('Start State called: Hello')

    # Use non-blocking sleep (correct for asyncio)
    yield from asyncio.sleep(0.1)

    # Deterministically transition to the 'World' state
    final_message = yield from world_coroutine()

    # The result is returned back up the call stack after all nested calls complete
    print('Coroutine completed. Final message received: ' + final_message)


@asyncio.coroutine
def world_coroutine():
    """Middle state: prints 'World' and transitions to the final state."""
    output_value = ' World'

    yield from asyncio.sleep(0.1)
    print('...evaluating...')

    # Deterministically transition to the '!' state
    exclamation = yield from exclamation_coroutine()

    # Append the result from the next state and return
    return output_value + exclamation


@asyncio.coroutine
def exclamation_coroutine():
    """End state: prints '!' and terminates the sequence."""
    output_value = '!'

    yield from asyncio.sleep(0.1)
    print('...stop computation...')

    return output_value


if __name__ == '__main__':
    print('Finite State Machine (FSM) Hello World simulation with Asyncio Coroutines')
    loop = asyncio.get_event_loop()
    
    # Run the main coroutine until it completes
    loop.run_until_complete(start_coroutine())
    loop.close()
    
    