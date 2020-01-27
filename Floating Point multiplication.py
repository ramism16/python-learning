def main():
    
    a=float(input("\nEnter the integer factor: "))
    b=float(input("Enter the real number factor: "))
    
    def product():
        
        multiple=a*b
        print("\n"+str(a),"multiplied with",str(b),"is =",round(multiple,3))
        
    product()
    
    
main()

input("")