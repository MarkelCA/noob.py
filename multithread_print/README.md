# Multithread print

This is a test to print a script's output in a separate thread, so the execution of the script gets boosted due to the saved output operations in the main thread

There are two approaches:
- print all but in a separate thread
- don't print the progress until requested from the user. If requested print in a separate thread

The ultimate goal of these tests are to create a decorator which runs the decorated function in a separate thread excluding the output and prints the current state when requested by the user
