print("\t\tWelcome to Spicy Sunday's!")

print("\nYou have been directed to the individual ice cream section.")
print("Please read the menu and pick your flavour.")

input("\t\nPress enter to view the menu")

print("\nChoice #1: Chocolate","(1)")
input("")
print("Choice #2: Banana","(2)")
input("")
print("Choice #3: Strawberry","(3)")
input("")
print("Choice #4: Green Tea flavour","(4)")
input("")

print("Flavour codes are printed next to the flavour.")

flavour=input("\nEnter the flavour code you see next to your flavour: ")

unlimit=0

while unlimit>-1:
    
    if flavour=="1":
        print("\nChocolate - Good choice!")
        break

    elif flavour=="2":
        print("\nBanana - Banana Terrific!")
        break

    elif flavour=="3":
        print("\nStrawberry - It's Okay...")
        break

    elif flavour =="4":
        print("\nGreen Tea - BIG mistake.")
        break

    else:
        print("\nWrong or no choice")
        flavour=input("\nEnter the flavour code you see next to your flavour: ")
    

input("\nPress enter to proceed to billing and checkout.")