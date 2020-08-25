def smallest_square(arg):
    n = 0
    while 2**n < arg:
        n = n + 1
    return n


print(smallest_square(2))    # Output: 1
print(smallest_square(7))    # Output: 3
print(smallest_square(32))   # Output: 5
print(smallest_square(100))  # Output: 7
print(smallest_square(801))  # Output: 10
