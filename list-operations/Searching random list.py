#Ramis Mustafa©

def random_list(n):
    import random
    X=[]
    for i in range(0,int(n)):
        X.append(random.randrange(0,10000))
    return X

def search(X,inp):
    flag=0
    total=0
    for j in range(0,len(X)):
        if inp==X[j]:
            flag=1
            total+=1
    if flag!=0:
        print(inp,"found in list",total,"number of times")
    else:
        print(inp,"not found in list")
    
def main():
    n=input("Enter the size of your list: ")
    while not n.isnumeric():
        print("Wrong input")
        n=input("Enter the size of your array: ")
    X=random_list(n)
    print("I have made a list of size",n)
    print("The list is full of random positive numbers from 0 to 10000")
    print("You can now search a number from the list")
    going="YES"
    while going.upper()=="YES" or going.upper=="YE" or going.upper=="Y":
        inp=input("\nEnter the value you want to search: ")
        while not inp.isnumeric():
            print("\nWrong input")
            inp=input("Enter the value you want to search: ")
        search(X,inp)
        going=input("\nDo you want to search any other number? ")
       
    input("\nPress enter to exit")

main()
