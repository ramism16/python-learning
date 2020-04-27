n=int(input("Enter the integer for factorial value: "))

if n>=0:
    ans=int(n)
    for i in range(1,n,1):
        ans=ans*i
    print("Factorial value is: "+str(ans))
else:
    print("Invalid input entered program will terminate on another false entry.")