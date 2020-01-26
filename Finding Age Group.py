print("\tEnter you're age to find your age group")

Age=int(input("\nEnter your age here: "))

input("Press enter... ")

if Age<18:
    print("You are a child!")
else:
    if Age<65:
        print("You are an adult!")
    else:
        if Age<100:
            print("You are a senior!")
        else:
            print("You are a centenarian!")

input("\nPress enter to exit")
