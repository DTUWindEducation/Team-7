def goldilocks(bed_length):
    if bed_length < 140:
        print("The bed is too small. Goldilocks is unhappy!")
    elif bed_length > 150:
        print("The bed is too large. Goldilocks is unhappy!")
    else:
        print("The bed is just right. Goldilocks is happy!")

bed_length = int(input("bed_lenght is (cm): "))
goldilocks(bed_length)


    