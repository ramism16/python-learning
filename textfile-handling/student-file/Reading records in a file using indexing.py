#display all records in a file
#main menu program[two]
def main():
    print("\nHere are all the records")
    stud_file=open("Student.txt", "r")
    student_record=[]
    student_record=stud_file.readlines()
    for i in range(0,len(student_record)):
        print(student_record[i])
        stud_id=student_record[i][0:4]
        stud_grade=student_record[i][4:7]
        stud_name=student_record[i][7:]
        print(stud_id)
        print(stud_grade)
        print(stud_name)
    stud_file.close()
    
main()
input("")

