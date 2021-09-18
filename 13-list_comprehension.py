#List comprehension
#print all the values of list  except "car"

mylist = ["car", "bus", "van"]

newlist=[x for x in mylist if x!="car"]
print(newlist)
