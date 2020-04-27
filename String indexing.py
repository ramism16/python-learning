#demo string indexing

word=str(input("Please enter a word of at least 10 characters: "))
print("Your word is",str(word),"It's length is:",int(len(word)))
lv=len(word)
for n in range(0,lv):
    print("Word [",n,"]\t=",word[n])

"""
alternate approach:
    i = 0
    for n in word:
        print("Word ["+ str(i) +"]\t = ", n)
"""

input("\npress enter to exit")