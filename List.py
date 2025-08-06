"""
l1 = [1,8,7,2,21,15] 
• l1.sort(): updates the list to [1,2,7,8,15,21] 
• l1.reverse(): updates the list to [15,21,2,7,8,1] 
• l1.append(8): adds 8 at the end of the list  
• l1.insert(3,8): This will add 8 at 3 index 
• l1.pop(2): Will delete element at index 2 and return its value. 
• l1.remove(21): Will remove 21 from the list. 

"""
# List is like array but only difference is that list can store multiple datatype at a same time
list = ["Dhrumil",7,8.95,True]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
# List is mutable i.e it can be changed after it is created
list[3]=False;
print(list[3])  # prints: False

# Tuples
"""
a = (1, 7, 2) 
• a.count (1): a count (1) will return number of times 1 occurs in a. 
• a.index (1) will return the index of first occurrence of 1 in a.

"""
# Tuples are immutable i.e it can't be changed after it is created
tuple1 =() #empty tuple
tuple2 = (1,) #tuple with one element need comma
tuple3= (1,2,3) #tuple with multiple element