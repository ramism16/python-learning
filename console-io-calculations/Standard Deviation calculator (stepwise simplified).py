print("Enter 5 integers below to get their sum, average and their standard deviation.",end="\n")
num1=int(input("First number: "))
num2=int(input("Second number: "))
num3=int(input("Third number: "))
num4=int(input("Fourth number: "))
num5=int(input("Fifth number: "))

#A built-in function "sum" is available, hence, "Sum" is used.

def Sum(a,b,c,d,e):
    S=a+b+c+d+e
    return(S)

def average(a,b,c,d,e):
    S=Sum(a,b,c,d,e)
    A=S/5
    return(A)

#For standard deriviation, simplicity for programmers is applied and the population for entities (numbers) is whole.

def strdev(a,b,c,d,e):
    A=average(a,b,c,d,e)
    va_a=(a-A)**2
    va_b=(b-A)**2
    va_c=(c-A)**2
    va_d=(d-A)**2
    va_e=(e-A)**2
    variance=(Sum(va_a,va_b,va_c,va_d,va_e))/5
    deviation=(variance**0.5)
    return(deviation)

#input("") is used as a wait function, or a promptless command

def main():
    print("The sum of the five numbers is",Sum(num1,num2,num3,num4,num5))
    input("")
    print("And there average is",average(num1,num2,num3,num4,num5))
    input("")
    print("And there standard deviation is",round(strdev(num1,num2,num3,num4,num5),4))

main()

input("Press enter to exit")