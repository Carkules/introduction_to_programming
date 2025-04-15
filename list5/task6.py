"""
Write a function which checks if a given list as an argument is sorted.
"""
def sort_check(x):
    return x == sorted(x)

print(sort_check(['a', 'b', 'c']))