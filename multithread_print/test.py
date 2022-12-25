import threading

max_count = 10000000
lock = threading.Lock()
count = 0

def your_method_with_a_loop_with_file():
    global count
    with open("f.txt","w") as f:
        for q in range(max_count):
            f.write(str(q)+"\n")
            #your_logic_here
            #....
            lock.acquire()
            count = count + 1
            lock.release()
            
def your_method_with_a_loop():
    global count
    for q in range(max_count):
        #your_logic_here
        #....
        lock.acquire()
        count = count + 1
        lock.release()

#Run the loop in a background thread
t1 = threading.Thread(target=your_method_with_a_loop)
t1.start()

while t1.is_alive():
    print("Press enter to see current loop iteration count\n")
    #use raw_input() instead if your are using python 2.x.
    input() #Remove this line if you want to print progress continuously.
    lock.acquire() 
    current_count = count
    lock.release()
    print("Current loop iteration count is ",count,"\n")

