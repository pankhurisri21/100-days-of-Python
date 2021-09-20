
#List Sorting
#sort() sorts in ascending order by default

#alphabetical sorting

mylist=["Delhi","Pune","Mumbai","Bangalore"]
print("Original list \n"+str(mylist))
print("\n")

#ascending order alphabetical sorting*
print("Ascending order - Alphabetically sorted list")
mylist.sort()
print(mylist)  #['Bangalore', 'Delhi', 'Mumbai', 'Pune']
print("\n")

#descending order alphabetical sorting*
print("Descending order - Alphabetically sorted list")
mylist.sort(reverse=True)
print(mylist) #['Pune', 'Mumbai', 'Delhi', 'Bangalore']
print("\n")

