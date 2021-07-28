def silly_encrypter(input):
    input_arrays = input.split(" ")
    silly_string = ""

    for val in input_arrays:
        val_firstLetter = val[0]
        
        silly_string = silly_string + " " + val.lstrip(val_firstLetter) + val_firstLetter + "IE"

    return silly_string


def silly_decrypter(input):
    input_arrays = input.split(" ")
    regular_string = ""

    for val in input_arrays:
        val_stripped = val.rstrip("IE")
        val_lastLetter = val_stripped[len(val_stripped)-1]
        val_stripped = val_stripped.rstrip(val_lastLetter)

        regular_string = regular_string + " " + val_lastLetter + val_stripped

    return regular_string


def main():
    input_string = input("Input a string to silly-fy ")
    print("English Input:", input_string)
    print("Silly Encryption output:", silly_encrypter(input_string))

    proceed = input("Do you want to reverse a silly string (y/n)?").lower()
    if proceed == "y":
        silly_input = input("Input silly string: ")
        print("Silly Input:", silly_input)
        print("Silly decryption output:", silly_decrypter(silly_input))


main()
