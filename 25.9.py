# # Find the min_element from the given list [4,3,24,5,2,7]
# li = [4,3,24,5,2,7]
# min = li[0]
# for num in li:
#     if num<min:
#         min = num
# print(min)



# # # Find the min_element from the given list [4,3,24,5,2,7]
# li = [4,3,24,5,2,7]
# min1 = li[0]
# min2 = li[0]
# for cur_num in li:
#     if cur_num<min1:
#         min2 = min1
#         min1 = cur_num
#     elif cur_num < min1 and cur_num > min2:
#         min2 = cur_num
# print(min2)




# # Create a list of 10 number and sum of all number.
# li = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range (len(li)):
#     sum += li[i]
# print(sum)



# # Find the largest and smallest num in list
# li = [1,2,3,4,5,6,7,8,9,10]
# smallest = li[0]       
# largest = float('-inf')   #infinity
# for cur_num in li:
#     if cur_num < smallest:
#         largest = smallest
#         smallest = cur_num
#     elif cur_num > largest and cur_num != smallest:
#         largest = cur_num
# print("smallest:", smallest)
# print("Largest:", largest)


# # WAP to reverse the list without using slicing
# li = [2,3,4,5,6,7,10,9,8] # This is in descending
# newarr = sorted(li, reverse = True)
# print(newarr)


# # or

# li = [1,2,3,4,5,6,7,8,9,10]
# left = 0 
# right = len(li) -1
# while left < right:
#     li[left],li[right] = li[right],li[left]
#     left += 1
#     right -= 1
# print(li)



# # Remove all duplicate numbers from list = [1,2,2,3,4,3,5]
# dl = [1,2,2,3,4,3,6,5] # duplicate_list
# un = [] # unique list
# for num in dl:
#     if num not in un:
#         un.append(num)
# print(un)




# # Find the second largest element from the given list [4,3,24,5,2,7]
# li = [1,2,3,4,5,6,7,8,9,10]
# largest1 = 0
# largest2 = 0
# for cur_num in li:
#     if cur_num>largest1:
#         largest2 = largest1
#         largest1 = cur_num
#     elif cur_num < largest1 and cur_num > largest2:
#         largest2 = cur_num
# print(largest2)




# # Merge the two list and sort the result
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [2,1,2,3,4,]
# l1.extend(l2) # list_2
# l1.sort()
# print(l1)






# WAP to find commond element from two list
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [2,1,2,3,4,]
comm = []
for num in l1:
    if num in l2:
        comm.append(num)
print(comm)


# WAP to print all even number in the li  = [1,2,3,4,5,6,7,8,9,10]
# li  = [1,2,3,4,5,6,7,8,9,10]


