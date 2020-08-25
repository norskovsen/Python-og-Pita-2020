name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name} in 20 years you will be {age+20}")
print("Hello {} in 20 years you will be {}".format(name, age+20))
print(f"Hello %s in 20 years you will be %d" % (name, (age + 20)))
