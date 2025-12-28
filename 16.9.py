# #this is print "updown"
# sent = "This is good for py"
# for alphabet in sent:
#     print(alphabet)

# # or 
# #this is print "updown"
# sent = "This is good for py"
# for c in sent:
#     print(c)



# #This is print "in a single line"
# sent = "This is good for py"
# for c in sent:
#     print(c, end="")


# #Print all even num from 1 to 100,, "1 to 100 print"
# for i in range (1,101):
#     print(i)


# #Print all even num from 1 to 100 and this is print odd
# for i in range (1,101,2):
#     print(i)



# #Print all even num from 1 to 100 and this is print even
# for i in range (1,101):
#     if i % 2 == 0:
#         print(i, end=" ")



# #Sentence = " I am an Indian and belong to jaipur."
# # Count the vowel of this sentence "13"
# Sentence = " I am an Indian and belong to jaipur."
# vowels = "aeiouAEIOU"
# count = 0
# for c in Sentence:
#     if c in vowels:
#         count += 1
# print(count) #13 vowels



# # Sentence = " I am an Indian and belong to jaipur." Print in reverse using for_loop
# Sentence = "I am an Indian"
# start = 0
# end = len(Sentence) - 1
# for i in range(end, start ,-1):
#     print(Sentence[i],end = "")



# # not true
# #sentence = "ReGex is epftware organisation" count the word here wiil be "4"
# sentence = "ReGex is epftware organisation".split()
# count = 0
# for word in sentence:
#     count += 1
# print(count)


# #Print number prime
# num = int(input("Enter the number "))
# for i in range(2, num):
#     if num%i == 0:
#         print("This is not prime")
#         break
#     else:
#         print("This is Prime")
#         break



# #Print number prime 100 to 1 but also odd number
# # num = int(input("Enter the number"))
# for num in range(100, 2 ,-1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#         else: 
#             print(num, end=" ")
#             break



# #userInput = "password@123"
# #attempt 3... again input the correct password 
# attempts = 3
# userInput = input("Enter your password: ")
# password = "password123"
# for i in range(1, attempts + 1):
#     if userInput != password:
#         print(f"Attempts left {attempts}")
#         userInput = input("Enter your password again: ")
#     else:
#         print("You have entered you correct password.")
#         break



# #userInput = "password@123" this is other method
# #attempt 3... again input the correct password 
# attempts = 3
# userInput = input("Enter your password: ")
# password = "password123"
# for i in range(1, attempts + 1):
#     if userInput != password:
#         attempts = attempts - 1
#         userInput = input("Enter your password again: ")
#         print(f"You have  {attempts} left")
#     else:
#         print("You have entered you correct password.")
#         break

