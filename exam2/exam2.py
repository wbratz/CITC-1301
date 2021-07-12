# for num in range(2, 9, 2):
#     print(num)

# for num in range(4):
#     print(num)

# for num in range(0, 20, 5):
#         num += num
# print(num) 

# for num in range(4):
#     print(num)

# for num in range(1, 5):
#     print(num)



# student = 1
# while student <= 3:
#     total = 0
#     for score in range(1, 4):
#         score = int(input("Enter: "))
#         total += score
#     average = total/3
#     print("Student ", student, "average: ", average)
#     student += 1

# total = 0
# for count in range(1, 4):
#     total += count
# print(total)

def main():
    average = findAverage()
    print(average)

def findAverage():
    number = 0
    loops = 0
    total = 0

    while number != -1:
        number = int(input("Enter a number: "))
        if(number != -1):
            total += number
            loops += 1

    return total/loops

main()

