def main():
    
    employ_no=input('Enter employee number: ')
        #validation, 10 characters only
    
    while not len(employ_no)==10:
        print("Wrong input")
        employ_no=input('Enter employee number: ')
       
    name=input('Enter employee name: ')
        #validation, 2 extra spaces for upper bound, provision for spaces
    
    while not len(name)>=2 and len(name)<=22:
        print("Wrong input")
        employ_no=input('Enter employee name: ')
            
    shift=input("Enter employee's shift: ")
    basic_pay=float(input('Enter basic pay: '))
    house_rent=basic_pay*0.4
    tax=basic_pay*0.1
    gross_salary=basic_pay+house_rent
    net_salary=gross_salary-tax
    print("House rent in Rs.:",house_rent)
    print("Net salary in Rs.:",net_salary)
    print("Tax in Rs.:",tax)
    print("Gross salary in Rs.",gross_salary)
    
    
main()

input("Press enter to exit")
