def main():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    
    if is_equal(first, second):
        print("equal")
    else:
        print("not equal")
    

def is_equal(first, second):
    if first == second:
        return True
    else:
        return False


main()
