#variables and datatypes

#python variables are case sensitive
print("\n\nPython variables are case sensitive")
a=20
A=45
print("a =",a)
print("A =",A)


a=20#integer
b=3.33 #float
c="hello" #string
d=True #bool

#type of value
print("Type of different values")
print("Type of :",str(a)+" =",type(a))
print("Type of :",str(b)+" =",type(b))
print("Type of : "+str(c)+ " =",type(c))
print("Type of : "+str(d)+" =",type(d))

#Type conversion
print("New Type of:",a,end=" = ")
print(type(str(a)))

print("New Type of:",b,end=" = ")
print(type(int(b)))
