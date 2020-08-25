# Python og Pita workshop 2020 - TODO
- [Link til slides](https://docs.google.com/presentation/d/1QwZ_1nFgREZk3raEFPRpUNxN8wlyvoeR7H4Fi6NIhrk/edit#slide=id.g62210f0158_3_30)
- Kode eksempler ligger i `eksempler` mappen
- Man kan også bruge følgende [notebook](https://colab.research.google.com/drive/18Ux2nuOxjlSxSdinqL0JHhgqL5dVqEoK)

## Installation af Python 3
- **Windows:** https://realpython.com/installing-python/#windows
- **MacOS:** https://realpython.com/installing-python/#macos-mac-os-x
- **Linux:** https://realpython.com/installing-python/#linux

## Opgaver - TODO
### Opgave a
Lav en funktion `my, der tager to nummer og addere dem sammen
### Opgave b
Lav en funktion, der udregner den euklidiske afstand mellem to punkter `p` og `q`. Punkterne representeres, som en tuple af `x` og `y` koordinaterne. Afstanden kan udregnes vha. følgende formel:
![distance](img/distance.gif)

**Skabelon**
```python
from math import sqrt

def distance(p, q):
    pass

print(distance((2,1),(4,1)))    # Output: 2.0
print(distance((4,3),(3,20)))   # Output: 17.029...
print(distance((14,10),(0,11))) # Output: 14.036...
print(distance((13,18),(12,8))) # Output: 10.049...
```

### Opgave c
Lav en funktion, som tager et beløb `amount`, en rente `interest_rate` og en månedlige betaling `montly_payment` og udregner hvor mange måneder det vil tage at betale og hvor penge der er til overs til sidst. (Funktion kan risikere at køre for evigt, hvis rente af lånet overstiger den månedlige betaling)

**Skabelon**
```python
def calculate_loan(amount, interest_rate, monthly_payment):
    pass


print(calculate_loan(2000, 0.01, 200))   # output: (11, -82.03...)
print(calculate_loan(100, 0.02, 200))    # output: (1, -98.0)
print(calculate_loan(10000, 0.10, 2000)) # output: (8, -1435.88...)
```

### Opgave d - TODO
Lav en funktion, der givet et brugernavn `username`, en adgangskode `password`, et navn `name` og en alder `age` og tjekker at:
- Brugernavnet har højest længde 12
- Adgangskoden har mindst længde 10
- Navnet er enten `None` eller har højest længde 12
- Alderen er enten -1 eller positiv

**Skabelon**
```python
def check_credentials(username, password, name = None, age = -1):
    pass


print(check_credentials("username", "securepassword"))                           # Output: True
print(check_credentials("toolongusername", "1234567890"))                        # Output: False
print(check_credentials("bob12", "1234"))                                        # Output: False
print(check_credentials("jensen", "longpassword", name = "Poul Hans Jensen"))    # Output: False
print(check_credentials("therealadam", "mynameisadam", name = "Adam", age=-23))  # Output: False
print(check_credentials("alice16", "6E&3sWXn2dnlv4", name = "Alice", age=20))    # Output: True
```

### Opgave e - TODO
Lav en funktion, som tjekker hvorvidt en liste `lst` er sorteret. 

**Skabelon**
```python
def is_sorted(lst):
    pass


print(is_sorted([17, 23, 27, 19, 31, 11])) # Output: False
print(is_sorted([1, 24, 26, 30, 33]))      # Output: True
print(is_sorted([9, 30, 39, 43, 43, 44]))  # Output: True
print(is_sorted([18, 14, 16, 5, 25]))      # Output: False
```



## Brugbare biblioteker

- Math: https://docs.python.org/3/library/math.html
- Mypy: http://mypy-lang.org/
- Sympy: https://www.sympy.org/en/index.html
- Numpy: https://docs.scipy.org/doc/numpy/reference/
- Matplotlib: https://matplotlib.org/contents.html
- iPython: https://ipython.readthedocs.io/en/stable/

