def main():

    user_selection = 0

    while user_selection != 5:
        print_menu()
        # If user does not select exit
        user_selection = get_menu_option()
        if user_selection != 5:
            #set initial values
            init_value = 0
            calc_value = 0
            from_value = ""
            to_value = ""

            # feet to yards
            if user_selection == 1:
                from_value = "feet"
                to_value = "inches"
                init_value = get_initial_value(from_value)
                calc_value = feet_to_inches(init_value)

            # yards to feet
            elif user_selection == 2:
                from_value = "yards"
                to_value = "feet"
                init_value = get_initial_value(from_value)
                calc_value = yards_to_feet(init_value)

            # handle getting the value for both mile conversions
            elif user_selection == 3 or user_selection == 4:
                from_value = "miles"
                init_value = get_initial_value(from_value)            

                # miles to yards
                if user_selection == 3:
                    to_value = "yards"
                    calc_value = miles_to_yards(init_value)

                #miles to feet
                if user_selection == 4:
                    to_value = "feet"
                    calc_value = miles_to_feet(init_value)

            print_calc(to_value, calc_value, from_value, init_value)

    print_exit()


def print_menu():
    print("1. Convert feet to inches")
    print("2. Convert yards to feet")
    print("3. Convert miles to yards")
    print("4. Convert miles to feet")
    print("5. Exit")


def print_exit():
    print("Goodbye.")


def print_calc(convert_to, calc_value, convert_from, init_value):
    print("There are {val1} {str1} in {val2} {str2}.".format(val1 = calc_value, str1 = convert_to, val2 = init_value, str2 = convert_from))


def get_menu_option():
    return int(input("Please choose a menu option: "))


def get_initial_value(measurment_name):
    return int(input("Enter the number of " + measurment_name + ": "))


def feet_to_inches(val):
    return val * 12


def yards_to_feet(val):
    return val * 3


def miles_to_yards(val):
    return val * 1760


def miles_to_feet(val):
    return val * 5280


main()

