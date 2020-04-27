def random_list(n):
    import random
    X=[]
    for i in range(0,int(n)):
        X.append(random.randrange(0,10000))
    return X

def myStrcopy(a):
    b=[]
    for i in range(0,len(a)):
        b.append(a[i])
    return b

def main():
    n=input("Enter the size of your list: ")
    while not n.isnumeric():
        print("Wrong input")
        n=input("Enter the size of your list: ")
    X=random_list(n)
    print("\nI will now copy the contents of your list to another list")
    print("I am now printing the list")
    Y=myStrcopy(X)
    print("\n",Y)

main()
input("Press enter to exit")
