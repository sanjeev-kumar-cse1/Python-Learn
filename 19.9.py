# # 1..
# n = 5   # height

# for i in range(n):
#     for j in range(2 * n - 1):
#         if j >= n - i - 1 and j <= n + i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # 2..
# n = 5  # height of half diamond

# # upper part
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# # lower part
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)

# # 3..
# #     1
# #   1 2 3
# # 1 2 3 4 5
# #   1 2 3
# #     1
# n = 3  

# # upper half including middle
# for i in range(1, n + 1):
#     # spaces
#     for j in range(n - i):
#         print(" ", end=" ")
#     # numbers
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()

# # lower half
# for i in range(n - 1, 0, -1):
#     # spaces
#     for j in range(n - i):
#         print(" ", end=" ")
#     # numbers
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()


# # 4..
# #         0 
# #       0 1 2 
# #     0 1 2 3 4 
# #   0 1 2 3 4 5 6 
# # 0 1 2 3 4 5 6 7 8 

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ", end =" ")
        
#     for j in range(2*i-1):
#         print(j, end=" ")
#     print()







# # 5..
# # A 
# # AB 
# # ABC 
# # ABCD


# for i in range(1, 3 + 1):
# # n = int(input("Enter number of rows: "))
# # for i in range(1, n + 1):
#     for j in range(65, 65 + i):   
#         print(chr(j), end="")
#     print()


# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         if i == j or j == n - 1 - i or i==0 or i==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




