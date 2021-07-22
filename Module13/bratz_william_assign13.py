
# added option to enter file name in the event you wanted to try the exception handling ;) 
try:
    grades_file = open(input("Enter File Name: "), "r")
except IOError as err:
    # exited here because if it can't read the file there is no reason to run
    print(err)
    exit()

gradeLine = grades_file.readline().rstrip()
highest_grade = ["", 0]
records = 0

while gradeLine != "":
    records += 1
    
    name_grade_list = gradeLine.split(";")
    
    try:

        if int(highest_grade[1]) < int(name_grade_list[1]):
            highest_grade = name_grade_list

    except ValueError as err:
        # I didn't know if you wanted to exit on this
        # I opted not to because the file could have multiple good entries and 1 bad
        print(err) 

    gradeLine = grades_file.readline().rstrip()

grades_file.close()

print("Highest Score: " + highest_grade[0] +", " + highest_grade[1])
print("Number of records:", records)

