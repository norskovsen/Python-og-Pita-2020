grade_pairs = (("Bob", 12), 
          ("Alice", 12),
          ("Charlie", 4), 
          ("David", -3), 
          ("Elise",4), 
          ("Elsa", 7),
          ("James", 0))

for name, grade in grade_pairs:
    if grade == 12:
        print(f"{name} got 12!")

    if grade == 0 or grade == -3:
        print(f"{name} failed the exam!")



