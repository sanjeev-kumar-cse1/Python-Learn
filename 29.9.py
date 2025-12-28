# li = [1,2,3,4]
# y = li
# #This modify old list and generate the same address
# y.append(5)
# print(id(li)) # 2133947980032
# print(id(y)) # 2133947980032
# print(y)




# li = [1,2,3,4]
# # It create a new list 
# x = li + [5] # This line not effect on old list and crate new object
# print(id(li)) # create new address
# print(id(x)) # create new address
# print(x) 




# a  = [1,2,3,4]
# b = a
# print(a is b) # True 



# a  = [1,2,3,4]
# b = a + [5]
# print(a is b)  # True



# # Deep Copy and shallow copy
# import copy
# li = [1,2,3,4]
# # This is shallow copy
# li1 = copy.copy(li)
# li1[0] = 10
# print(li1) # [10, 2, 3, 4]




# import copy
# li = [1,2,3,4]
# # This is shallow copy
# li1 = copy.copy(li)
# li1[0] = 10
# print(id(li)) # diff. diff.address store
# print(id(li1)) # diff. diff.address store
# print(li1)



# import copy
# li = [1,2,3,4]
# # This is shallow copy
# li1 = copy.copy(li)
# li1[0] = 10 
# print(li) # [1, 2, 3, 4]



# # 2-D list 
# li = [[1,2,3],[4,5,6]]
# print(li[0]) # [1,2,3]
# print(li[1]) # [4, 5, 6]



# li = [[1,2,3],[4,5,6]]
# s = li[0][1]
# print(s) # 2





# li = [[1,2,3],[4,5,6]]
# li[0][1]
# print(len(li)) # 2



# li = [[1,2,3],[4,5,6]]
# li[0][1]
# for i in range(len(li)):
#     print(li[i]) # [1, 2, 3]
#                 # [4, 5, 6]





# # [1, 2, 3]
# # 1
# # 2
# # 3
# # [4, 5, 6]
# # 4
# # 5
# # 6
# li = [[1,2,3],[4,5,6]]
# li[0][1]
# for i in range(len(li)):
#     # print(li[i])
#     for j in range(len(li[i])):
#         print(li[i][j])





# li = [1,2,3]
# for i in range(len(li)):
#     print(li[i]) # 1 2 3 in column




# # sum of all elements from 2-D list 

# li = [[1,2,3],[4,5,6]]
# li[0][1]
# sum = 0
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         sum += (li[i][j])
# print(sum) # 21 






# #Print all the even number from the list



# # Search any elements from the list 2 exist -> This num is present in (i,j)

# li = [2,3,45,5]
# target = 45
# for i in range(len(li)):
#     if target == li[i]:
#         print(i) # 2 index




# li = [[1,2,3],[4,5,6]]
# t = 2
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if t == li[i][j]:
#             print(i,j) # 1 2 "1 is row, and 2 is column"




# Shallow copy and Deep copy

# import copy
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) # Diff. diff address due to this is shallow copy
# print(id(li)) # 1827783156160
# print(id(new)) # 1827783031104



# import copy
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) # Here is same address
# print(id(li[0][1])) # 140724911532504
# print(id(new[0][1])) # 140724911532504




# import copy
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) 
# new[0][1] = 100 
# print(li) # [[1, 100, 3], [4, 5, 6]]



# # Shallow copy me jo outer obj uska new obj create ho jate hai but nested object ke new references create nhi hote. 
# import copy 
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) # Here is same address
# new[0][1] = 100 
# print(id(li[0])) # 2362621038976
# print(id(new[0])) # 2362621038976





# import copy 
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) # Here is same address
# new.append([4,5,6])
# print(li) # Same list [[1, 2, 3], [4, 5, 6]]
# print(new) # [[1, 2, 3], [4, 5, 6], [4, 5, 6]] appended elements are also come in new




# import copy 
# li = [[1,2,3],[4,5,6]]
# new = copy.copy(li) 
# new1 = copy.deepcopy(li)
# new1[0][1] = 200
# print(li) # Same list [[1, 2, 3], [4, 5, 6]]
# print(new1) # [[1, 200, 3], [4, 5, 6]] 




word = "This is asnasi".split()
word.reverse()
print(word())
