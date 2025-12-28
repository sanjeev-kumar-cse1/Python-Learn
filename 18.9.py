# # hello
# # hello
# # hello
# # hello
# # hello
# # hello
# count = 0
# while True:
#     if count == 10:
#         break 
#     print("hello")
#     count += 1

# #Reversing the  list using while_loop
# li = [1,2,3,4,5]
# left = 0
# right= len(li)-1
# while left < right:
#     li[left], li[right] = li[right], li[left]
#     left += 1
#     right -= 1
# print(li)  # here if print(li) is not then only li present


# #Hollow triangle user input
# n = int(input("Enter rows: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print("# ", end="")
#         else:
#             print("  ", end="")
#     print()


# #Hollow triangle 
# for i in range(5 ):
#     for j in range( i + 1):
#         if i == j or j == 0  or i == 4:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()


# # Hollow Rectangle
# rows = 5
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()




#             *  
#          *  *
#       *  *  *
#    *  *  *  *
# for i in range(1, 5):
#     for j in range( 5- i):
#             print("  ", end=" ")
#     for k in range (i):
#             print("* ", end=" ")
#     print()


# # or 
# n = 5
# for i in range(1, n+1):
#     for j in range( n- i):
#             print("  ", end=" ")
#     for k in range (i):
#             print("* ", end=" ")
#     print()







