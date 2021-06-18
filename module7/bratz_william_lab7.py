is_valid = False

while not is_valid:
    name = input("Put something in here that meets criteria: ")
    
    if name.isalpha() and 5 <= len(name) <= 10:
        is_valid = True
    else:
        print("Invalid username! Please try again.")

print("Username accepted")


