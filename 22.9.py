# #    *    
# #   *  *
# #  *    *
# # *      *
# #  *    *
# #   *  *
# #    *
# n= 7
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i+j == (n // 2)+2 or i-j == (n // 2) or j-i == (n // 2) or i+j == (n+(n//2)+1):
#             print("* ", end="" )
#         else:
#             print(" " , end="")
#     print()




# # WHILE_LOOP guessing number
# n = 7
# num = int(input("Enter a number: "))
# while True:
#     if n !=  num:
#         num = int(input("Enter correct number: "))
#     else:
#         print("You have guessed number!")
#         break



# 1.. print all even number 1 to 100
# for i in range(2, 101, 2):
#     print(i, end=" ")


# or
# i = 2  
# while i <= 100:
#     print(i, end=" ")
#     i += 2

# or 
# n = 100
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1


# # 2.. Ask user input the 5 number , if the number is -ve then skip it don't count it and print all these 5 numbers.
# count = 0
# numbers = []
# total = 0

# while count < 5:
#     num = int(input(f"Enter number {count+1}: "))
#     if num < 0:
#         print("Negative number skipped!")
#         continue   
#     numbers.append(num)
#     total += num
#     count += 1

# print("The 5 valid numbers are:", numbers)
# print("Sum of numbers =", total)



# # 3.. find the LCM of two number.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# lcm = num1 if num1 > num2 else num2

# while True:  
#     if lcm % num1 == 0 and lcm % num2 == 0:   
#         print(f"LCM of {num1} and {num2} is {lcm}")
#         break
#     lcm += 1   





# # 4.. find the GCD (Greatest common Divisor) of two number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

print(num1)   

