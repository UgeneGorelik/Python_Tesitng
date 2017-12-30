#an example of testing Performance

#import libs
import time
import random
import  statistics


#functions to check performance from them
def sum(n):
    time.sleep(0.0001)
    return n+n

def minus(n):
    time.sleep(0.0001)
    return  n - n

def mult(n):
    time.sleep(0.0001)
    return  n * n

def divide(n):
    time.sleep(0.0001)
    return n//n

#create dictionary with function name and list of times of running
funcs_to_test=sum,minus,divide,mult
total_stats = {}

for x in funcs_to_test:
    total_stats[x.__name__]=[]


#ran each function at random for the purpose of checking how different types of warmup affects
#results  


for x in range(1,100):
    func_to_run_now=random.choice(funcs_to_test)
    function_start_time=time.time()
    func_to_run_now(x)
    function_end_time=time.time()
    total_time=abs((function_end_time*10000-function_start_time*10000)*100000)
    total_stats[func_to_run_now.__name__].append(total_time)
    #runtimes[func_to_run_now.__name__].append((function_end_time-function_start_time)*1000)



#print median ,mean and deviation
for f_name,f_result in total_stats.items():
    print('function name :', f_name, 'Used', len(f_result), 'times')
    print('\t median of run', statistics.median(f_result))
    print('\t mean of run  ', statistics.mean(f_result))
    print('\t standart deviation ', statistics.stdev(f_result))



