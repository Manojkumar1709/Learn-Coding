# Write a Python program to implement a stopwatch. The program should start timing when the user presses ENTER and 
# stop timing when the user interrupts with Ctrl+C, displaying the elapsed time in seconds.

import time

def stopwatch():
    print("Press ENTER to start the stopwatch.")
    print("Press Ctrl+C to stop the stopwatch.")
    
    try:
        input("Press ENTER to start...")
        start_time = time.time()  
        print("Stopwatch started...")
        
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        try:
            end_time = time.time()  
            total_time = end_time - start_time
            print(f"Total Time: {total_time:.2f} seconds")
        except NameError:
            print("\nStopwatch was not started.")

if __name__ == "__main__":
    stopwatch()
