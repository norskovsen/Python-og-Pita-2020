def all_positive_even_numbers(lst):
    for numb in lst:
        if numb % 2 != 0:
            return False
        if numb <= 0:
            return False

    return True


print(all_positive_even_numbers([2, 4, 10, 12]))
print(all_positive_even_numbers([4, 6, 11, 13]))
