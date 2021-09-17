#Adding values to list 

languages=['Hindi','English','Arabic','French']
print(languages) #['Hindi', 'English', 'Arabic', 'French']

#insert()
languages.insert(3,"Spanish") #inserts at specific index
print(languages) # ['Hindi', 'English', 'Arabic', 'Spanish', 'French']

#append()
languages.append("Japanese") #inserts or appends at the end of the list
print(languages) #['Hindi', 'English', 'Arabic', 'Spanish', 'French', 'Japanese']


#extend()
mylist1=["apple","papaya"]
print(mylist1) #['apple', 'papaya']
mylist2=["pineapple","banana"]
print(mylist2) #['pineapple', 'banana']
mylist1.extend(mylist2)
print(mylist1) #['apple', 'papaya', 'pineapple', 'banana']

