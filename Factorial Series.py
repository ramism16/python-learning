import math

print("This program will evaluate the sum of the sequence n/!n (end number/(factorial of end number) based on your input")
input("")

print("For example: ( 1/!1 + 2/!2 + 3/!3 )= 2.5")
input("")

n=int(input("\nType in the end number of the sequence as an integer, greater than 0: "))

inputs=1
ans=0

while inputs<5:
    if n>0:
        for i in range(0,n-1):
            ans=((i)/((math.factorial(i))))
        print("Sum of sequence is = "+str(ans))
        break
    else:
        print("Wrong input value, try again. Program exits at five wrong entries.")
        n=int(input("\nType in the end number of the sequence as an integer, greater than 0: "))
        inputs=inputs+1

input("Press enter to quit")