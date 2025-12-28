# # Shallow copy
# import copy
# li = [[1,2,3], [4,5,6]]
# copied = copy.copy(li)
# #outer object reference 









# # Nested object reference of the original list
# print(id(li[0]))
# # Nested object reference of the copied list
# # # sice this is shallow copy that's why 




# copied.append([7,8,9])
# print(li)
# print(copied)

# copied[0][0] = 100

# copied
# print(copied)




# # Deep Copy
# import copy
# original_list = [[1,2,3,4], [5,6,7,8]]
# #Deep copying the oringinal list
# new_list = copy.deepcopy(original_list)
# #Since the references are different , that's why the new outer object is created
# print(id(original_list))
# print(id(new_list))
# # Checking the nested object
# print(id(original_list[0]))
# print(id(new_list[0]))
# # Checking the nested object using "f-string"
# print(f' Id of the original nested object -> {id(original_list[0])}')
# print(f'Id of the new nested object -> {id(new_list[0])}')




# # Tuple: This is a built in data structure in python that is used to store the multiple Element in a single variable
# # It is the similar to the list 
# # This is never change
# # Contain also duplicate element
# # This is faster than list -> In tuple memory is fixed 
# # Dynamic memory
# # Represented by " t = () "

# t = ()
# print(type(t)) # <class 'tuple'>

# t = (1, 'ram', 4.6)
# print(t) # (1, 'ram', 4.6)

# # Tuple is ordered, it means indexing is posssible (Element is fixed postion)
# t = (1, 'ram', 4.6)
# print(t[0])


# t = (1, 'ram', 4.6)
# print(t[0])
# print(t[1])
# print(t[2])



# t1 = (1)
# print(type(t1)) # <class 'int'>



# t1 = ('ram',)
# print(type(t1)) # <class 'tuple'>




# t2 =  (1,1,'tuple', "tuple", 5.5, 5.5)
# print(t2) # (1, 1, 'tuple', 'tuple', 5.5, 5.5)



# # Creating tuple with list 
# li = [1,2,3,4,5]
# t3 = tuple(li)
# print(type(t3))
# print(t3)
# print(li)


# Accessing element
# t4 =  (1,2,3,4,5)









# # Tuple operation
# t1= (1,2,3)
# t2 = (4,5,6)
# t3 = t1 + t2 # Concatenating the two tuple using "+"operator
# print(t3) # (1, 2, 3, 4, 5, 6)



# t4 = (1,2)
# t5 = t4 * 5 #  Repeating-Time
# print(t5) # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)



# # Membership operator: in, not in

# t6 = (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# if 7 not in t6:   # YES
#     print("yes")
# else:
#     print("Not")



# t6 = (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# if 7 in t6:  # NOT
#     print("yes")
# else:
#     print("Not")


# # This method takes value as argument and return the index element 
# t7 = (1,2,3,4,5)
# t = t7.index(5) # 4
# print(t)



# # Count element how many time
# t8 = (1,2,2,3,4,5,4,3,7,8,9,7,6,6)
# t = t8.count(6)
# print(t)



# # Tuple packing 
# a = 'Sanjeev',10, 5.5, 7
# print(type(a)) #<class 'tuple'>



# # Tuple unpaking
# a, b,c,d = 'Sanjeev',10, 5.5, 7
# print(a)
# print(b)
# print(c)
# print(d)




# # Nested Tuple
# t7 = (1,2,(3,4),5,(6,(7,8)))
# t = t7[4][1][0]
# print(t) # 7



# # Iterating over the Tuples
# t = (1,2,3,4)
# for i in range (len(t)): # Iterating over the Tuples using index
#     print(t[i])
# for element in t: 
#         print(element)
        