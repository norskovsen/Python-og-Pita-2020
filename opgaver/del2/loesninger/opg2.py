from math import sqrt

def is_prime(n):
    return len([i for i in range(2,1+int(sqrt(n))) if n % i == 0]) == 0

print(is_prime(7))  # Output: True
print(is_prime(16)) # Output: False
print(is_prime(23)) # Output: True
print(is_prime(42)) # Output: False
