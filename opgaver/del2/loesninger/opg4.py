class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age} years old)"

    def __gt__(self, other):
        return self.age > other.age

person1 = Person("Alice", 17)
person2 = Person("Bob", 19)
person3 = Person("Charles", 24)

print(person1)           # Output: "Alice (17 years old)"
print(person2)           # Output: "Bob (19 years old)"
print(person3)           # Output: "Charles (24 years old)"
print(person1 > person3) # Output: False
print(person2 > person1) # Output: True
