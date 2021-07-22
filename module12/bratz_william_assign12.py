## Code to generate number list, this was easier than actually making one :D
# numbers = open("numbers.txt", "w")

# for number in range(1, 101):
#     numbers.write(str(number) + "\n")

# numbers.close()

file_name = open(input("Enter the file name to read from: "), "r")

bad_numbers = []
target_numbers = []

number_list = file_name.readlines()

for number in number_list:
    if int(number) >= 25 and int(number) <= 75:
        target_numbers.append(number.rstrip())
    else:
        bad_numbers.append(number.rstrip())

file_name.close()

print("Target numbers: ")
print(target_numbers)
print("Bad numbers: ")
print(bad_numbers)

