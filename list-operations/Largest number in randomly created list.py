#Ramis Mustafa ©

def random_list(n):
    import random
    X=[]
    for i in range(0,int(n)):
        X.append(random.randrange(0,10000))
    return X

def largest(X):
    length=len(X)
    largest_number=0
    filtered_list=[]
    for i in range(0,len(X)-1):
        for j in range(0,len(X)-1):
            if X[j+1]<X[j]:
                filtered_list.append(X[i])
    largest_number=filtered_list[-1]
    return largest_number

def main():
    again="Y"
    while again.upper()=="Y" or again.upper()=="YES" or again.upper()=="YE":
        n=input("Enter the size of your list: ")
        while not n.isnumeric():
            print("Wrong input")
            n=input("Enter the size of your list: ")
        X=random_list(n)
        print("I have made a list of size",n)
        print("The list is full of random positive numbers from 0 to 10000")
        input("\nPress enter to continue")
        W=largest(X)
        print("\nI will now find the largest number in random list")
        input("\nPress enter to know the largest number")
        print("The largest numvber in the list is:",W)

        again=input("\nDo you want to try this procedure with another list? ")

        input("Press enter to exit")


main()
        
        
    

        
