from math import sqrt


def distance(p, q):
    return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


print(distance((2, 1), (4, 1)))     # Output: 2.0
print(distance((4, 3), (3, 20)))    # Output: 17.029...
print(distance((14, 10), (0, 11)))  # Output: 14.036...
print(distance((13, 18), (12, 8)))  # Output: 10.049...
