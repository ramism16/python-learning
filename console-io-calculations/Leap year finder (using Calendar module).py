import calendar

year=int(input("Enter the year to know if it is a leap year: "))

import calendar
crit=calendar.isleap(year)

if crit==True:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")

input("\nPress enter to exit")