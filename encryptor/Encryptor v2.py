def replay():
    #The encryptor simplified
    #The intro
    print("This program will display the encrypted output for your string.")
    MessageString=str(input("\nEnter a message string for encryption: "))
    Length=int(len(MessageString))

    #The arrays            
    Alphabet=[]
    for i in range(65,91):
        Alphabet.append(chr(i))
    substitute=['P','L','F','N','O','C','Q','U','D','Z','V','G','I','X','M','W','J','B','K','E','A','H','S','Y','R','T']

    #Provision for space character in the arrays
    Alphabet.append(chr(32))
    substitute.append(chr(32))

    #Validation
    valid=False
    while valid==False:
        for j in range(0,Length):
            if MessageString[j].upper() in Alphabet:
                valid=True
            else:
                print("Wrong input")
                MessageString=str(input("\nEnter a message string for encryption: "))
            
    #The encryption
    Encryption=[]
    indexes=[]
    for k in range(0,Length):
        for l in range(0,len(Alphabet)):
            if MessageString[k].upper()==Alphabet[l]:
                Encryption.append(substitute[l])

    #The output
    print("The encryption has been done")
    print(''.join(Encryption))

#Defined prodecures to repeat the encryptor
def main():
    Choice="Y"
    while not Choice.upper() in ["N","NO"]:
        replay()
        Choice=input("\nDo you want to encrypt any other string? Y/N ")
    input("\nPress enter to exit")

main()
