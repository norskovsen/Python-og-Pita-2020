def check_credentials(username, password, name = None, age = -1):
    pass


print(check_credentials("username", "securepassword"))                           # Output: True
print(check_credentials("toolongusername", "1234567890"))                        # Output: False
print(check_credentials("bob12", "1234"))                                        # Output: False
print(check_credentials("jensen", "longpassword", name = "Poul Hans Jensen"))    # Output: False
print(check_credentials("therealadam", "mynameisadam", name = "Adam", age=-23))  # Output: False
print(check_credentials("alice16", "6E&3sWXn2dnlv4", name = "Alice", age=20))    # Output: True
