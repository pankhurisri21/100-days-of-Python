#Program to print current date  and  provided date and date components

#current date

from datetime import date
today=date.today()
print("Today's date is",today)


print("Year = "+str(today.year)+" "+"Month = "+str(today.month)
+" "+"Day = "+str(today.day))

#provided date
my_date=date(2021,12,21)
print("My date is:",my_date)


print("Year = "+str(my_date.year)+" "+"Month = "+str(my_date.month)+" "+"Day = "+str(my_date.day))
