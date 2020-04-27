import math

Num=int(input("Input the integer for the factorial value: "))
if Num >=0:
    input("Press enter for factorial value ")
else:
    print("\nNegative integer is unacceptable, program will stop on false entry...")
    Num=int(input("Input a positive integer for the factorial value: "))

if Num==0 or Num==1:
    print("\n\tFactorial value is 1")
else:
    print("\n\tFactorial value is",math.factorial(Num))

input("\nPress enter to exit")