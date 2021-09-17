#Accessing list items

mybag=["book","copy","pen","bottle","lunchbox"]

#indexing
print(mybag[1]) #'copy'
#forward indexing starts from 0

#negative indexing
print(mybag[-1])  #'lunchbox'
#backward indexing starts from -1

#range of index
print(mybag[1:4])  # ['copy','pen','bottle']
#start index included,  end index excluded


#takes value from starting to (end_index-1)
print(mybag[:4])  #['book','copy','pen','bottle']


#takes value from start index to last index of list
print(mybag[2:])  #['pen','bottle','lunchbox']
