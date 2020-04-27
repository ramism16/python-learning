def reverse(N):
    Reversed=[]
    for i in range(-1,-1-len(N),-1):
        Reversed.append(N[i])
    return Reversed

def make_array():
    N=[]
    funcstop=0
    print("Add positive integer to list, enter negative integer to stop adding:",end="\n")
    while funcstop>=0:        
        funcstop=int(input(""))
        if funcstop>=0:
            N.append(funcstop)
    return N

def main():
    N=make_array()
    Reversed=reverse(N)
    print("Your list")
    print(N)
    print("\nhas been reversed to obtain")
    print(Reversed)
    
        
main()

input("")
