def main():
    print("Input three different integers to know which is the smallest")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    num3=int(input("Enter third number: "))

    
    if num1<num2:
        if num1<num3:
            print("\nFirst number",num1,"is the smallest")
        else:
            print("\nThird number",num3,"is the smallest")

    else:
        if num2<num3:
            print("\nSecond number",num2,"is the smallest")
        else:
            print("\nThird number",num3,"is the smallest")
        

    
main()

input("\n\nPress enter to exit")
