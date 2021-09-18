#List comprehension

mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]
'''output
apple
banana
cherry
'''
#or
newlist=[x for x in mylist]
print(newlist) # output ['apple', 'banana', 'cherry']
