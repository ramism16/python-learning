def main():
    c=str(input("Enter one character: "))  
    while not len(c)==1:
        print("\nWrong input")
        c=str(input("Enter one character: "))

    print("Character",c,"is entered which is represented by",ord(c),"in ASCII decimal table")

main()

input("\n\nPress enter to exit")
      
