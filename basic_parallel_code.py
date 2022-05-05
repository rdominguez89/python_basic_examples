from pebble import ProcessPool

from timeit import default_timer as timer
import numpy as np

def function_1(var_1,var_2,array_1,array_2,max_workers):
    numbers_work_at_once = int(len(var_1)/max_workers)
    results_all = np.zeros(len(var_1))
    ir=0
    with ProcessPool(max_workers=max_workers) as pool:
            future = pool.map(function_2,var_1,var_2,len(var_1)*[array_1],
                               len(var_1)*[array_2], chunksize=numbers_work_at_once, timeout=100)
            iterator = future.result()
            while True:
                try:
                    result = next(iterator)
                    results_all[ir] = result
                    ir = ir + 1
                except StopIteration:
                    print("END")
                    break
    return results_all

def function_2(var_1,var_2,array_1,array_2):
    sum = 0
    for i in range(len(array_1)):
        sum = sum + var_1 + var_2 + array_1[i] + array_2[i]
    return sum

#target = '',target = 'cpu',target = 'parallel',target = 'cuda'
#It in neccesary to specify where is going to run
@vectorize(["float64(float64,float64,float64,float64)"],target='')
def VectorAdd_2(var_1,var_2,array_1,array_2):
    return var_1 + var_2 + array_1 + array_2
