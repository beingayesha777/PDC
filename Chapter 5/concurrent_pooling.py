import concurrent.futures
import time
import random


WORD_LIST = ["Hello", "World"]


def print_message(word):
    """
    A simple function that simulates a small amount of work and prints a word.
    
    NOTE: We use time.sleep() here to simulate I/O bound work, which is why
    ThreadPoolExecutor will often show performance gains over sequential execution.
    For true CPU-bound work, ProcessPoolExecutor is superior.
    """
    # Simulate a small, non-CPU-intensive delay (I/O bound simulation)
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    
    print(f'Processed: {word} (Slept for {delay:.2f}s)')
    return f'{word} completed.'


def evaluate_futures(item):
    """
    Wrapper function to call print_message and manage output.
    """
    # Call the print function
    result_item = print_message(item)
   
    return result_item


if __name__ == '__main__':
    print("--- Concurrent Futures 'Hello World' Demonstration ---")
    
    # --- 1. Sequential Execution (Blocking) ---
    print("\n--- 1. Sequential Execution ---")
    start_time = time.perf_counter()
    
    for item in WORD_LIST:
        evaluate_futures(item)
        
    end_time = time.perf_counter()
    print(f'Sequential Execution took {end_time - start_time:.4f} seconds')

    
    # --- 2. Thread Pool Execution (Best for I/O bound tasks like sleep/network) ---
    print("\n--- 2. Thread Pool Execution (Parallel I/O Simulation) ---")
    start_time = time.perf_counter()
    
    # Set max_workers to the length of the list to ensure they all run immediately
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks and collect futures
        futures = [executor.submit(evaluate_futures, item) for item in WORD_LIST]
        
        # Wait for all futures to complete (map/as_completed is also an option)
        concurrent.futures.wait(futures)
        
    end_time = time.perf_counter()
    print(f'Thread Pool Execution took {end_time - start_time:.4f} seconds')
    
    
    print("\n--- 3. Process Pool Execution (Parallel CPU Simulation) ---")
    start_time = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        # Using executor.map is often cleaner for simple lists of arguments
        list(executor.map(evaluate_futures, WORD_LIST))
        
    end_time = time.perf_counter()
    print(f'Process Pool Execution took {end_time - start_time:.4f} seconds')