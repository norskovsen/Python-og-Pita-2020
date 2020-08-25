def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


print(is_sorted([17, 23, 27, 19, 31, 11])) # Output: False
print(is_sorted([1, 24, 26, 30, 33]))      # Output: True
print(is_sorted([9, 30, 39, 43, 43, 44]))  # Output: True
print(is_sorted([18, 14, 16, 5, 25]))      # Output: False
