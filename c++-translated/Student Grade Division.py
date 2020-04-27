def main():
    
    marks=[]
    
    for i in range(1,6):    
        print("\nEnter the marks for subject",i,end="\n")
        m=float(input())
        
        if m>=0 and m<=100:
            marks.append(m)
        else:
            print("\nWrong input,enter marks for subject",i,end="\n")
            m=float(input())
            


    per=float((sum(marks)/500.0)*100)

    if per>=60:
        print("\nStudent is in first division")
    elif per>=50:
        print("\nStudent is in second division")
    elif per>=40:
        print("\nStudent is in Third division")
    else:
        print("\nStudent has failed")

main()

input("\n\nPress enter to exit")