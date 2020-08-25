def binary_search(lst, elm):
    res = -1
    left = 0
    right = len(lst)
    while left != right:
        mid = (right - left) // 2 + left

        if lst[mid] == elm:
            res = mid
            break

        if lst[mid] > elm:
            right = mid
        else:
            left = mid

    return res 

print(binary_search([12, 13, 18, 28, 31, 33, 35, 37, 45, 47], 45))     # Output: 8
print(binary_search([0, 2, 8, 12, 16, 17, 29, 32, 37, 39], 12))        # Output: 3
print(binary_search([4, 14, 17, 23, 24, 29, 32, 35, 42], 4))           # Output: 0
print(binary_search([3, 5, 12, 29, 31, 37], 31))                       # Output: 4
