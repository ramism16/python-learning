print("\t\t\tEnter numbers for comparison")

Num1=float(input("Enter Integer 1:"))
Num2=float(input("\nEnter Integer 2:"))

input("\n\tPress Enter")

if Num1==Num2:
    print("\nNumber 1 ("+str(Num1)+") is equal to Number 2 ("+str(Num2)+")")
else:
    if Num1>Num2:
        print("\nInteger 1 ("+str(Num1)+") is larger than Number 2 ("+str(Num2)+")")
    else:
        print("\nInteger 2 ("+str(Num2)+") is larger than Integer 1 ("+str(Num1)+")")
        
input("\n\nPress enter to exit")