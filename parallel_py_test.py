# Author:
# Sleiman Safaoui
# Github: 
# The-SS
# Email:
# snsafaoui@gmail.com 
# sleiman.safaoui@utdallas.edu

#
# Demonstrates how to use the multiprocessing.Process python function to run several instances of a function in parallel
# The script runs the same number of instance of the function in series and parallel and compare the execution time
# Note: Running a small number of instance will not demonstrate the advantages of parallel processing
#

from __future__ import print_function
import multiprocessing as mp
import time


def function1(num1, num2): # function to run multiple instances of
    sum1 = 0
    if num1 < num2:
        for i in range(num2 - num1):
            sum1 += 1
    elif num2 < num1:
        for i in range(num1 - num2):
            sum1 += 1
    else:
        sum1 = 0

    print('returning: ', sum1)
    return sum1


def run_parallel_instances(number_of_instances_to_run):
    '''
    runs several instances of function1 in parallel
    '''
    
    cpu_count = mp.cpu_count()  # get number of CPUs available
    print(cpu_count, ' available. Will use all of them')

    start_time = time.time()  # for timing
    
    all_events = []
    for count in range(1, number_of_instances_to_run):
        event = mp.Process(target=function1, args=(1, (count * count) ** 3))  # start a process for each function (target takes function name and args is the arguments to pass)
        event.start()  # start the function but don't wait for it to finish
        all_events.append(event)  # store handle for the process

    for e in all_events:
        e.join()  # join the parallel threads
    end_time = time.time()

    print('Ran ', number_of_instances_to_run, 'parallel instances')
    print('Finished Parallel processes in: ', end_time - start_time)
    return end_time - start_time


def run_sequential_instances(number_of_instances_to_run):
    '''
    runs several instances of function1 sequentially
    '''
    
    start_time = time.time()
    
    for count in range(1, number_of_instances_to_run):
        function1(1, (count * count) ** 3)
    end_time = time.time()
    
    print('Ran ', number_of_instances_to_run, 'sequential instances')
    print('Finished Sequential processes in: ', end_time - start_time)
    return end_time - start_time


if __name__ == "__main__":
    number_of_instances_to_run = 20
    s_time = run_sequential_instances(number_of_instances_to_run)
    p_time = run_parallel_instances(number_of_instances_to_run)

    print('Sequential time: ', s_time)
    print('Parallel time: ', p_time)
