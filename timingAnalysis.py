def timingAnalysis(func, start, stop, inc, runs):
    '''prints average run times of function func on inputs of seize start,
     start+inc, start+2*inc, ..., up to stop'''
    times = []
    for n in range(start, stop, inc): # for every inút size
        acc = 0.0                                  # initialize accumulator

        for i in range(runs):  #repeat rusn times:
            acc += timing(func, n) # run func on input of size n
                                   # and accumulates run times

        # print average run times foor input size n
        formatStr = 'Run time of {}({}) is {:.7f} seconds.'
        print(formatStr.format(func.__name__, n, acc/runs))
        yield(acc/runs)
       
        


import time
from matplotlib import pyplot as plt
def timing(func, n):
    'runs func on input returner by buildInput'
    funcInput = buildInput(n) # obtain input for func

    start = time.time()
    func(funcInput)
    end = time.time()

    return end - start



def buildInput(n):
    'returns input for Fibonacci functions'
    '''this function takes an input size and returns an object that is
    an appropriate input for function func() and has the right
    input size.'''
    return n
    

def rfib(n):
    'returns nth Fibonacci number'
    if n < 2:                     # base case
        return 1

    return rfib(n-1) + rfib(n-2)  # recursive step


def fib(n):
    'returns nth Fibonacci number'
    previous = 1     # 0th Fibonacci number
    current = 1      # 1st Fibonacci number
    i = 1            # index of current Fibonacci number

    while i < n:     # while current is not nth Fibonacci number
        previous, current = current, previous+current
        i += 1

    return current

if __name__ == '__main__':
    func1 = 'fib'
    func2 = 'rfib'
    times1, times2 = [], []
    genTimes1 = timingAnalysis(fib, 24, 31, 2, 10)
    genTimes2 = timingAnalysis(rfib, 24, 31, 2, 10)
    n = list(range(24, 31, 2))
    times1 = list(genTimes1)
    times2 = list(genTimes2)
    print(times2)
    print(times1)    
    plt.plot(n, times1)
    plt.plot(n, times2)
    plt.show()
    
    
