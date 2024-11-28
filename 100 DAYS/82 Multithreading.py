'''Multithreading in Python'''

# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.


'''Creating a thread'''
# To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method. Here's how we can create a simple thread.
'''
import threading
def my_func():
  print("Hello from thread", threading.current_thread().name)
  thread = threading.Thread(target=my_func)
  thread.start()
  thread.join()
'''
# Functions
# The following are some of the most commonly used functions in the threading module:

# threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.

# threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.






'''Creating multiple threads'''

# Creating multiple threads is a common approach to using multithreading in Python. The idea is to create a pool of worker threads and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process tasks in parallel.
'''
import threading
def thread_task(task):
    # Do some work here
    print("Task processed:", task)
if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threads = []
    for task in tasks:
        thread = threading.Thread(target=thread_task, args=(task,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
'''

### Using a lock to synchronize access to shared resources

# When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads. A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code. The lock is released when the thread finishes executing the critical section.
'''
import threading

def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()

if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()

    threads = []
    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Counter value:", counter)
'''


'''Conclusion'''
# As you can see, the threading module provides a simple and efficient way to implement multithreading in Python. Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources, the threading module has you covered.

# In conclusion, the threading module is a powerful tool for 'parallelizing' code in Python. Whether you are a beginner or an experienced Python developer, the threading module is an essential tool to have in your toolbox. With multithreading, you can take advantage of multiple CPU cores and significantly improve the performance of your code.


# CODE 

# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor


# # # Indicates some task being done
# def func(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)
#   return seconds


# def main():
#     time1 = time.perf_counter()
# #   Normal Code
#     # func(4)
#     # func(2)
#     # func(1)

# #   Same code using Threads
#     t1 = threading.Thread(target=func, args=[4])
#     t2 = threading.Thread(target=func, args=[2])
#     t3 = threading.Thread(target=func, args=[1])
#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()
#     # Calculating Time
#     time2 = time.perf_counter()
#     print(time2 - time1)


# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(func, 3)
#     # future2 = executor.submit(func, 2)
#     # future3 = executor.submit(func, 4)
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     l = [3, 5, 1, 2]
#     results = executor.map(func, l)
#     for result in results:
#       print(result)


# poolingDemo()




# MY CODE


import threading
import time


# def fun1(seconds):
#     time.sleep(seconds)
#     print(f"function run after {seconds} seconds")

    
# # IF WE RUN NORMALLY THEN ONE BYE ONE FUNCITONS WILL EXECUTE, WHICH CAN MAKES OR OUR PROGRAM SLOW
# # fun1(5)
# # fun1(2)
# # fun1(4)


# # BY USING THREADING THE FUNCTIONS WILL RUN SIMULTANEOUSLY, WHICH CAN SAVE OUR TIME
# # THIS IS THE WAY HOW WE CAN IMPLEMENT A THREADING TO OUR FUNCITON
# f1 = threading.Thread(target=fun1,args=[4])
# f2 = threading.Thread(target=fun1,args=[2])
# f3 = threading.Thread(target=fun1,args=[5])

# # start() IS USED TO BEGIN THE IMPLEMANTATION OFA FUNCTION 
# f1.start()
# f2.start()
# f3.start()

# # join() JOIN IS USED WHEN WE WANT TO WAIT UNTIL ALL THE THRADING FUNCTION ARE COMPLETE RUNNING THEN GO TO NEXT PROGRAMM
# f1.join()
# f2.join()
# f3.join()

# THIS IS THE NORMAL WAY OF USING THE THREADNG AND IT INCREASES THE LINE OF CODE AS THE THREADIN FUNCTION INCREASES
# THEREFORE TO MAKE A CODE SMALL WE USE (MULTIPLE THREADING)
# FOR THIS WE HAVE TO IMPORT THE MODULE 

from concurrent.futures import ThreadPoolExecutor


def fun1(seconds):
    time.sleep(seconds)
    print(f"function run after {seconds} seconds")


# THIS IS THE WAY HOE WE CAN RUN THE TASK PARALLEL

with ThreadPoolExecutor() as executor:
    # task1 = executor.submit(fun1,5)
    # task2 = executor.submit(fun1,2)
    # task3 = executor.submit(fun1,4)
    # print(task1)                       # THIS IS ALSO LIKE THREADING USES THE MULTIPLE LINE, THERE FOR WE USE LISTING METHOD TO LESS DOWN THE 
    # print(task2)                       # NO. OF LINES OF CODE
    # print(task3)
    

    
    time1 = time.perf_counter()
    
    task_List = [5,2,4]
    tasks = executor.map(fun1,task_List)       # With list we use map() fucntion
    for task in tasks:
        print(task)
        
    time2 = time.perf_counter()
    print(f"program run in {time2-time1} seconds")
    

