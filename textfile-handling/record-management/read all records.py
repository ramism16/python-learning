def readfile():
    Sales=open("Sales.txt","r")
    sales_record=Sales.readlines()
    length=len(sales_record)
    Xtotal=[]
    Ytotal=[]
    choice=input("Press 1 to see all records from file, 2 for total of sales and 3 to quit: ")
    while not int(choice)==3:
        if int(choice)==1:
            for i in range(length):
                print(sales_record[i])
        elif int(choice)==2:
            for i in range(length):
                Xtotal.append(sales_record[i][11:14])
                Ytotal.append(sales_record[i][15:18])
            totalX=sum(Xtotal)
            totalY=sum(Ytotal)
            print("The total of SalesX is",totalX)
            print("The total of SalesY is",totalY)
        choice=input("Press 1 to see all records from file, 2 for total of sales and 3 to quit: ")

def main():
    readfile()

main()
