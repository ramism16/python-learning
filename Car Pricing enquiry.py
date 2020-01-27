#Car Salesman Program

print("\tPractice problems question 4")

print("\nEnter the baseprice of the car to look at the extra cost details below.")

base=float(input("\nBaseprice: $ "))

Tax=float(0.25*base)
print("\nTax(2.5%): $"+str(Tax))

License=float(0.005*base)
print("License(0.5%): $"+str(License))

Dealer_prep=float(54)

Destination_Charge=float(25)

total= base + Tax + License + Dealer_prep + Destination_Charge

print("\nTotal actual price: $", total)

input("Press enter to proceed")