#List Sorting

#numeric sorting 

mynumbers=[23,34,22,12,1,89,79]
print("Original list \n"+str(mynumbers))
print("\n")

#ascending order numeric sorting 

print("Ascending order - Numerically sorted list")
mynumbers.sort()
print(mynumbers) #[1, 12, 22, 23, 34, 79, 89]
print("\n")


#descending order numeric sorting 
print("Descending order - Numerically sorted list")
mynumbers.sort(reverse=True)
print(mynumbers) #[89, 79, 34, 23, 22, 12, 1]
print("\n")
