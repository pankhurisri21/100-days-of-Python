#Changing list values

languages=['Hindi','English','Arabic','French']
print(languages) #['Hindi', 'English', 'Arabic', 'French']

#Changing value of particular index
languages[1]='Spanish'
print(languages) #['Hindi', 'Spanish', 'Arabic', 'French']

#changing range of values
languages[1:3]=["Japanese","Portugese"] 
print(languages) #['Hindi', 'Japanese', 'Portugese', 'French']

#replacing large range of value with smaller range of  values
languages[1:3]=["German"] 
print(languages) #['Hindi', 'German', 'French']

#replacing through negative indexing
languages[-2:-1]=["Turkish"]
print(languages)
