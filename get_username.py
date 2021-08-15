import random
randnum=random.randint(0,1000)
name=input('Enter your name : ')
print("Your username is : "+ name[0:3]+"_"+str(randnum))
