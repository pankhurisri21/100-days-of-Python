  #remove()
  #pop()
  #del
  #clear()

mycolors=['red','blue','black','pink','white','purple']
mylist1=['apple','guava','banana']  
mylist2=['grapes','melon','kiwi']
mylist3=['pineapple']
  
#remove()
#removes specific item
mycolors.remove('red')
print(mycolors) #['blue', 'black', 'pink', 'white', 'purple']

#pop(index)
#removes item at specific index
mycolors.pop(1)
print(mycolors) #['blue', 'pink', 'white', 'purple']

#pop()
#removes last value from the list
mylist1.pop() 
print(mylist1) #['apple', 'guava']

#clear()
#removes all elements from the list
mylist2.clear()
print(mylist2) #[]

#del
#removes value at specific index
del[mylist1[0]]
print(mylist1) # ['guava']

#del listname
#deletes the whole list
del mylist3
#print(mylist3) #this will cause an error because you have succsesfully deleted "mylist3".
#NameError: name 'mylist3' is not defined

