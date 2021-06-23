def count_vowels(input):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for letter in input:
        if letter == "a":
            a += 1
        if letter == "e":
            e += 1
        if letter == "i":
            i += 1
        if letter == "o":
            o += 1
        if letter == "u":
            u += 1

    print("a: " + str(a))
    print("e: " + str(e))
    print("i: " + str(i))
    print("o: " + str(o))
    print("u: " + str(u))


entered_string = input("Enter a string and I'll tell you how many of each vowel it has: ")
count_vowels(entered_string.lower())


