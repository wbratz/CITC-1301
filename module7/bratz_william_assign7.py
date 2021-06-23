sentinel = 0
total = 0
maximum = 0

maximum = int(input("Enter the value for the maximum number: "))

while True:
    number = int(input("Enter a number between 1 and " + str(maximum) + " to add: "))

    if number > maximum or number == sentinel:
        print("Invalid Number")
    elif number < sentinel:
        break
    else:
        total += number

print("Sum of all the numbers you entered: ", total)
