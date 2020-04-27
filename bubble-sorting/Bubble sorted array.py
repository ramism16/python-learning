def make_array():
    array=[]
    funcstop=0
    print("Add positive integer to list, enter negative integer to stop adding:",end="\n")
    while funcstop>=0:        
        funcstop=int(input(""))
        if funcstop>=0:
            array.append(funcstop)
    return array

def print_big_enough(array,number):
    for i in range(0,len(array)):
        if array[i]<number:
            
    swapped=False
    while swapped==False:
        for counter in range(0,len(array)-1):
            for j in range(0,len(array)-1):
                if array[counter+1]<array[counter]:
                    array[counter+1],array[counter]=array[counter],array[counter+1]
        swapped=True
    return array,number

def main():
    array=make_array()
    number=int(input("Input the positive integer as your second parameter: "))
    print("\nI will now filter and sort your list.")
    print_big_enough(array,number)
    print("Your modified list is ")
    print(array)
    input("\n")

main()