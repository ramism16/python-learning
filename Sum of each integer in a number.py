num=int(input("Enter a five digit positive integer: "))

i=1
while i>0:
    
    if num>=10000 and num<=99999:
        print("\nI will now add each individual integer of your number")

        Anum=str(num) 
        Sum= 0

        for i in Anum: Sum += int(i)
        print("\nThe sum is",Sum)

        break
    
    else:
        print("Wrong input, try again")
        num=int(input("Enter a five digit positive integer: "))
        i=1
    
input("\nPress enter to exit")