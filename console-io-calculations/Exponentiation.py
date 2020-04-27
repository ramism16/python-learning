print("I will evaluate the value of base number raised by the exponent provided.")

def power(a,b):
    A=a**b
    return(A)

base=float(input("\nEnter the base number: "))
exponent=float(input("\nEnter the exponent/index value: "))
input("")
print(base,"raised to the power of",exponent,"is",round(power(base,exponent),3))

input('\nPress enter to exit')