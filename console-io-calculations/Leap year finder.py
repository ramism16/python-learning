year=int(input("Type the year to find if it is a leap year: "))

def leapyear(n):
    if n%400==0 or n%4==0:
        print(n, "is a leap year.")
    else:
        print(n,"is not a leap year.")
        
leapyear(year)

input("Press enter to exit")