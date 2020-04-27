#Delete a particular record from the file
#Main menu program[four]
def main():
    print("\nSearch an individual student record")
    stud_file=open("Student.txt", "r+")
    student_record=[]
    student_record=stud_file.readlines()
    length =len(student_record)
    search1="Y"
    yes_opt=["Y","y","yes","Yes","YES","yEs","YeS","YEs","yES","yeS"]
    while search1 in yes_opt:
        flag=0
        desireID=input("Enter student ID: ")
        while not len(desireID)==4:
            print("Wrong input")
            desireID=input("Enter student ID: ")
        for i in range(0,length):
            stud_id=student_record[i][0:4]
            stud_grade=student_record[i][4:7]
            stud_name=student_record[i][7:]
            if desireID in stud_id:
                print("Student ID:",stud_id)
                print("Student grade:",stud_grade)
                print("Student name:",stud_name)
                flag=1
                sure=input("Do you want to delete this entry? Y/N: ")
                if sure in yes_opt:
                    del student_record[i]
                break
        if flag!=1:
            print(desireID,":ID does not exist in records")
        search1=input("Do you want to search another student? Y/N: ")
        
    for j in range(length):
        stud_file.write(student_record[i])
    stud_file.close()
    
main()
input("")
