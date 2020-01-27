print("\tEnter the mass and volume to obtain Density in grams/cubic centimetre")

Mass=float(input("Enter the mass of the object(Number only): "))
Volume=float(input("\nEnter the displacement in water or known volume of the object(Number only): "))

Density= Mass/Volume

input("\nPress enter to calculate density")

print("\nDensity:", round(Density,3),"grams/cubic centimetre")

input("\nPress enter to exit")