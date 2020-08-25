def div_rest(a, b):
    integer_div = a//b
    div_rest = a % b
    return integer_div, div_rest

a, b = 11, 5
q, r = div_rest(a,b)
print(f"Division of {a} and {b} is {q} with remainder {r}")

