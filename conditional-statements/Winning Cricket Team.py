#Ramis Mustafa

print("This program will compare and display the winning cricket team based on runs.")

Team1=input("Type the team's name: ")

Team2=input("\nType the second team's name: ")

Runs1=int(input("\nType the runs for the first team: "))

Runs2=int(input("\nType the runs for the second team: "))

input("")
  
    
if Runs1==Runs2:
            
print("The match between",Team1,"and",Team2,"has drawn.")
            
elif Runs1>Runs2:
            
print(Team1,"has won the match by",str(Runs1-Runs2))
            
else:
            
print(Team2,"has won the match by",str(Runs2-Runs1))


input("Press enter to exit")

