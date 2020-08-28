numb = 5
a = 2

while a**2 < numb:
    if numb % a == 0:
        print(str(numb) + " is not a prime")
        break
    a += 1
else:
    print(str(numb) + " is a prime")
