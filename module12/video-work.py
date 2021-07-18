# Store data in files
# volitile memory
# persistant storage

# numbers = open('input.txt', 'r')

# lines = numbers.readlines();

# for line in lines:
#     print(line.rstrip())

# numbers.close()

# lines.append(numbers.readline().rstrip())

# line1 = numbers.readline().rstrip()
# line2 = numbers.readline().rstrip()
# line3 = numbers.readline().rstrip()
# line4 = numbers.readline().rstrip()

# numbers.close()


# print(line1)
# print(line2)
# print(line3)
# print(line4)

# movie_list = ["Scott Pilgrim vs The World\n", "O' Brother where art thou\n", "Something"]

# movies = open('output.txt', 'w')

# movies.write("Scott Pilgrim vs The World\n")
# movies.write("O' Brother Where art thou?\n")
# movies.write("")

# movies.close()
# print("Finished Writing to file")

numbers = open("numbers.txt", "w")

for number in range(1, 101):
    numbers.write(str(number) + "\n")

numbers.close()
