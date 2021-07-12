numbers = [83, 21, 103, 16, -8, 71, 82, 119, -35, 28]
valid_numbers = []

def get_valid_numbers(numbers):
    for number in numbers:
        if number > 0 and number <= 100:
            valid_numbers.append(number)


def get_total(numbers):
    total = 0

    for number in numbers:
        total += number
    
    return total


def get_average(numbers):
    return get_total(numbers)/len(numbers)


def main():
    get_valid_numbers(numbers)
    print(valid_numbers)
    total = get_total(valid_numbers)
    print("Total:", total)
    avg = get_average(valid_numbers)
    print("Average:", avg)

main()