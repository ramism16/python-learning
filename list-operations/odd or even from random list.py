#Ramis Mustafa©

def random_list(n):
    import random
    X=[]
    for i in range(0,int(n)):
        X.append(random.randrange(0,10000))
    return X

def odd_list(X):
    xodd=[]
    for i in range(0,len(X)):
        if X[i]%2!=0:
            xodd.append(X[i])
    return xodd

def even_list(X):
    xeven=[]
    for i in range(0,len(X)):
        if X[i]%2==0:
            xeven.append(X[i])
    return xeven

def main():
    n=input("Enter the size of your list: ")
    while not n.isnumeric():
        print("Wrong input")
        n=input("Enter the size of your list: ")
    X=random_list(n)
    print("I have made a list of size",n)
    print("The list is full of random positive numbers from 0 to 10000")
    input("\nPress enter to continue")
    print("\nNow you can print:")
    print("1: List of even numbers from your random list")
    print("2: List of odd number from your random list")
    xodd=odd_list(X)
    xeven=even_list(X)
    inp=int(input("\nEnter 1 to receive odd numbers' list, 2 for even and 3 to quit: "))
    while inp>0 and inp<4:
        if inp==1:
            print("Odd list is:")
            print("\n",xodd)
        elif inp==2:
            print("Even list is:")
            print("\n",xeven)
        elif inp==3:
            break
        inp=int(input("\nEnter 1 to receive odd numbers' list, 2 for even and 3 to quit: "))

    input("\nPress enter to exit")

main()
        
        
    
    


    
    
    
            
