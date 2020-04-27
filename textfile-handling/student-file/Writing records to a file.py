#Making/writing records to new/existing file
#Main menu program[one]
def main():
    print("\nAdding student info")
    stud_file=open("Student.txt","a")
    choice="Y"
    yes_opt=["Y","y","yes","Yes","YES","yEs","YeS","YEs","yES","yeS"]
    while choice in yes_opt:
        stud_id=input("Enter student ID: ")
        while not len(stud_id)==4:
            print("Wrong input")
            stud_id=input("Enter student ID: ")
        stud_name=input("Enter student name: ")
        while not len(stud_name)>=2:
            print("Wrong input")
            stud_name=input("Enter student name: ")
        stud_grade=input("Enter student grade: ")
        while not len(stud_grade)==3:
            print("Wrond input")
            stud_grade=input("Enter student grade: ")        
        student_record=(stud_id)+stud_grade.title()+stud_name+"\n"
        print(student_record)
        stud_file.write(student_record)
        choice=input("Do you want to add other records? ")
    stud_file.close()

main()
input("")

