#Display a particular student record
#Main menu program[three]
def search(lst):
    length =len(lst)
    search1="Y"
    yes_opt=["Y","y","yes","Yes","YES","yEs","YeS","YEs","yES","yeS"]
    while search1 in yes_opt:
        flag=0
        desireID=input("Enter student ID: ")
        while not len(desireID)==4:
            print("Wrong input")
            desireID=input("Enter student ID: ")
        for i in range(0,length):
            stud_id=lst[i][0:4]
            stud_grade=lst[i][4:7]
            stud_name=lst[i][7:]
            if desireID in stud_id:
                print("Student ID:",stud_id)
                print("Student grade:",stud_grade)
                print("Student name:",stud_name)
                flag=1
                break
        if flag!=1:
            print(desireID,":ID does not exist in records")
        search1=input("Do you want to search another student?")
    
def main():
    print("\nSearch an individual student record")
    stud_file=open("Student.txt", "r")
    student_record=[]
    student_record=stud_file.readlines()      
    search(student_record)
    stud_file.close()
    
main()
input("")

