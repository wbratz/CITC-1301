print("Enter a number 0 - 36")

user_entry = int(input())

if user_entry >= 0 and user_entry <= 36:
    if user_entry == 0:
        print("The monster color is: purple")
    elif user_entry >= 1 and user_entry <= 10:
        if (user_entry % 2) == 0:
            print("The monster color is: black")
        else:
            print("The monster color is: blue")
    elif user_entry >= 11 and user_entry <= 18:
        if (user_entry % 2) == 0:
            print("The monster color is: blue")
        else:
            print("The monster color is: black")
    elif user_entry >= 19 and user_entry <= 28:
        if (user_entry % 2) == 0:
            print("The monster color is: black")
        else:
            print("The monster color is: blue")
    elif user_entry >= 29 and user_entry <= 36:
        if (user_entry % 2) == 0:
            print("The monster color is: blue")
        else:
            print("The monster color is: black")
else:
    print("The value entered is invalid")