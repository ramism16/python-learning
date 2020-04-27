def new_studentrecord():
    Sales=open("Sales.txt","a+")
    choice="Y"
    import datetime
    yes_opt=["Y","YES","YE"]
    while choice.upper() in yes_opt:
        year = input('Enter a year (must be 4 digits): ')
        if len(year)!=4:
            print("Wrong input")
            year = input('Enter a year (must be 4 digits): ')
        month = input('Enter a month (add 0 if one digit): ')
        if len(month)!=2 or month<="0" or month>="12":
            print("Wrong input")
            month = input('Enter a month (add 0 if one digit): ')
        day=input('Enter a day (Enter 0 if one digit): ')
        if len(day)!=2 or day<="0" or day>"31":
            print("Wrong input")
            day=input('Enter a day (Enter 0 if one digit): ')
        Sale_Date = year+"/"+month+"/"+day
        SalesX=input("Enter value for SalesX: ")
        while not SalesX.isnumeric():
            print("Wrong input")
            SalesX=input("Enter value for SalesX: ")
        while not len(SalesX)<=3:
            print("Wrong input")
            SalesX=input("Enter value for SalesX: ")
        if len(SalesX)==1:
            SalesX="00"+SalesX
        elif len(SalesX)==2:
            SalesX="0"+SalesX
        SalesY=input("Enter value for SalesY: ")
        while not SalesY.isnumeric():
            print("Wrong input")
            SalesY=input("Enter value for SalesY: ")
        while not len(SalesY)<=3:
            print("Wrong input")
            SalesY=input("Enter value for SalesY: ")
        if len(SalesY)==1:
            SalesY="00"+SalesY
        elif len(SalesY)==2:
            SalesY="0"+SalesY
        sales_record=Sale_Date+","+SalesX+","+SalesY+"\n"
        Sales.write(sales_record)
        choice=input("Do you want to enter any other record? Y/N ")
    Sales.close()
        
def main():
    input("Press enter to add a record")
    new_studentrecord()
    

main()
