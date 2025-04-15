"""
Write a recursive and iterative functions that calculates first n elements of Fibonacci sequence.
Compare the running times of the functions for n = 100.
"""
import timeit

def rec_fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = rec_fibonacci(n-1)
    seq.append(seq[n-2]+seq[n-3])
    return seq
start = timeit.default_timer()
print(rec_fibonacci(100))
print(timeit.default_timer() - start)
    

def it_fibonacci(n):
    seq = []
    for i in range(n):
        if i == 0:
            seq.append(0)
        elif i == 1:
            seq.append(1)
        else:
            seq.append(seq[i - 1] + seq[i - 2])
    return seq
start = timeit.default_timer()
print(it_fibonacci(100))
print(timeit.default_timer() - start)