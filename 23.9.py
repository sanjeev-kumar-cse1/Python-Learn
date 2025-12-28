# # LCM
# num1 = 4
# num2 = 12
# num3 = 8
# lcm = 0
# if num1>num2>num3:
#     lcm = num1
# else:
#     lcm = num2 = num3
# while True:
#     if lcm % num1 == 0 and lcm % num2 ==0 and lcm % num3 == 0:
#         print(lcm)
#         break
#     lcm += 1



# # List of Grocery
# a = 'Toothpaste'
# b = 'soap'
# print(a)



# # list : list is the sequence data type which 

# li = ['soap', 'tooth', 'shampoo' ]
# print(li[0])
# print(li[1])
# print(li[2]) 



# dt =  ['sanjeev',  1,( 3+ 2j),12.2 ]
# print(dt[0])
# print(type(dt[0]))
# print(dt[1])
# print(type(dt[1]))
# print(dt[2])
# print(type(dt[2]))
# print(dt[3])
# print(type(dt[3]))




# dt =  ['Sanjeev',  1, ( 3+ 2j), 12.2 ]
# dt.append("Kumar") # When add some thing then use ".append" 
# dt.append(10)
# print(dt) # ['Sanjeev', 1, (3+2j), 12.2, 'Kumar', 10]



# dt =  ['Sanjeev',  1, ( 3+ 2j), 12.2 ]
# dt.append("Kumar") # When add some thing then use ".append" 
# dt.append(10)  # When add some thing then use ".append" 
# print(dt)

# print(len(dt)) #6

# dt.append([10,20])  # When add some thing then use ".append" 
# print(len(dt)) #7
# print(dt[6]) #[10,20]


# dt.extend([1,2,3,4,5,6]) # When add more then all add in "LIST" and use ".extend"
# print(dt)

# dt.insert(1,21)
# print(dt)

# dt.pop(5) # This is deleted that value which are as follow the indexing
# print(dt)

# dt.remove(5) # This deleted that value which are in real , means give that value direct which have to delete.
# print(dt)



# li = [2,3,4,5,6,7,10,9,8]
# li.sort()
# print(li)



# li = [2,3,4,5,6,7,10,9,8] # This is in descending
# newarr = sorted(li, reverse = True)
# print(newarr)



# Slicing into the LIST

# li = [2,3,4,5,6,7,10,9,8]
# print(li[1:7]) # This is as like as FOR_LOOP
# print(li[:7:2])




li = [2,3,4,5,6,7,10,9,8]
li[-1:3:-1] #Accessing last index value
print(li) 