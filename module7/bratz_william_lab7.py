is_valid = False

while not is_valid:
    name = input("Enter a username that has only alphabetical characters and is between 5 and 10 characters: ")
    
    if name.isalpha() and 5 <= len(name) <= 10:
        is_valid = True
    else:
        print("Invalid username! Please try again.")

print("Username accepted")


