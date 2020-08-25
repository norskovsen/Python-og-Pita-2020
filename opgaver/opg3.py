def sum_list(lst):
    res = 0
    for elm in lst:
        res = res + elm
    return res


print(sum_list([3, 0, 3]))           # Output: 6
print(sum_list([8, 8, 0, 7, 7, 8]))  # Output: 38
print(sum_list([2, 1, 8, 8, 8]))     # Output: 27
print(sum_list([1, 3, 3, 7, 2]))     # Output: 16
print(sum_list([4, 0, 5]))           # Output: 9
