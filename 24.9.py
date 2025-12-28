# # Index wise iteration in list
# li = [1,2,3,4,5,6]
# for i in range(len(li)):
    # print(li[i])



# # WAP to print the sum of all elements list = [1,2,3,4,5,6]
# li = [1,2,3,4,5,6]
# sum = 0
# for i in range (len(li)):
#     sum += li[i]
# print(sum)



# WAP to print all even number in the li  = [1,2,3,4,5,6,7,8,9,10]




# # Find the largest element in the li = [1,2,3,4,5,6,7,80,9,100]
# li = [1,2,3,4,5,6,7,80,9,100]
# largest = 0
# for num in li:
#     if num>largest:
#         largest = num
#         print(f"This is largest {largest}") # This is for checking / debudging.
# print(largest)


# # Find the second-largest element in the li = [1,2,3,4,5,6,7,8,9,10]
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



# # Find the largest element in the li = [1,2,3,4,5,6,7,8,9,10]
# li = [-1,-2,-3,-4,-5]
# largest = li[0]
# for cur_num in li:
#     if cur_num>largest:
#         largest = cur_num      
# print(largest)


# # Find the second-largest element in the li = [1,2,3,4,5,6,7,8,9,10]
# li = [-1, -2, -3, -4, -5]
# largest1 = li[0]       
# largest2 = float('-inf')   #infinity
# for cur_num in li:
#     if cur_num > largest1:
#         largest2 = largest1
#         largest1 = cur_num
#     elif cur_num > largest2 and cur_num != largest1:
#         largest2 = cur_num
# print("Largest:", largest1)
# print("Second Largest:", largest2)



# # Find the Third-largest element in unordered li = [1,2,3,4,5,6,7,8,9,10] ///not right code
# li = [1,2,3,4,5,6,7,8,9,10]
# first = li[0]
# second = li[0]
# third = li[0]
# for num in li:
#     if num > first:
#         third = second
#         second = first
#         first = num
#     elif num > second and num < first:
#         third = second
#         second = num
#     elif num > third and num < second:
#         third = num
# print("Largest three numbers are:", first, second, third)




# # Find the smallest element in the li = [1,2,3,4,5,6,7,8,9,10]
# li = [1,2,3,4,5,6,7,8,9,10]
# smallest = 2
# for num in li:
#     if num<smallest:
#         smallest = num
#         print(f"This is largest {smallest}") # This is for checking / debudging.
# print(smallest)





