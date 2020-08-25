def eval(x, a0 = 0, a1 = 0, a2 = 0):
    return a0 + x*a1 + x*a2**2

eval(2, a1=2)
eval(2, a0=1, a2=4)
