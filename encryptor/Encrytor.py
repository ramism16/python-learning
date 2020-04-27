#Ramis Mustafa
#Encryption using pseudocode
print("This program will display the encrypted output for your word.")


MessageString=str(input("\nEnter a message string for encryption: "))
LengthMessageString=int(len(MessageString))
Alphabet=[]
for i in range(65,91):
    Alphabet.append(chr(i))
substitute=['P','L','F','N','O','C','Q','U','D','Z','V','G','I','X','M','W','J','B','K','E','A','H','S','Y','R','T']
Encryption=[]
for j in range(0,LengthMessageString):
    for counter in range(0,26):
        if MessageString[j].upper()==Alphabet[counter]:
            ans=counter
            break
    Encryption.append(substitute[ans])


print("\nThe encrypted message is",end="\n")
print(''.join(Encryption))

input("")