# # Membership: Check given is present or not
# str = "aeiouAEIOU"
# s = input("Enter a string: ")
# if s in str:
#     print("Vowel")
# else:
#     print("Consonant")




# # Bihar is CEO from Sanjeev
# name = "Sanjeev"
# loaction = "Bihar"
# #.format() function
# # for string fromating 
# print("{1} is CEO from {0}".format(name, loaction))



# # Sanjeev is CEO from Bihar
# name = "Sanjeev"
# loaction = "Bihar"
# #.format() function
# # for string fromating 
# print("{1} is CEO from {0}".format(loaction, name))



# #reverse print "veejnaS"
# name = "Sanjeev"
# name[::-1]


# #Print reverse "Sanjeev is good -> separate word "
# name = "sanjeev is a good boy"
# s = name.split()
# print(s)



# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" #['boy', 'good', 'a', 'is', 'sanjeev']
# words = name.split()
# words.reverse()
# print(words)



# # Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()
# for i in range(0,5): #01234 in updown
#     print(i)



# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()
# for i in range(0,5 , 1): #01234 in updown
#     print(i)



# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for i in range(0,5, 2): #024 in updown
#     print(i)


# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for i in range(1, 5+1, 1): #12345 in updown
#     print(i)


# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for i in range(5+1,1,-1): #65432 in updown
#     print(i)


# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for i in range(5+1,0,-1): #654321 in updown
#     print(i)


# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for i in range(5+1,-1,-1): #6543210 in updown
#     print(i)




# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# words.reverse()

# for word in words: #Print reverse word in updown
#     print(word)



# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy" 
# words = name.split()
# # words.reverse()
# s = '.'.join(['as', 'df', 'lkj']) #as.df.lkj
# print(s)


# #Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy"  #boy good a is sanjeev
# words = name.split()
# words.reverse()
# reversed_sent = " ".join(words)
# print(reversed_sent)


# # Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy"  
# words = name.split()
# print(words) #['sanjeev', 'is', 'a', 'good', 'boy']
# words.reverse()
# reversed_sent = " ".join(words)
# print(reversed_sent)



# # Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy"  
# words = name.split()
# print(words) 
# words.reverse()
# print(words)
# reversed_sent = " ".join(words)
# print(reversed_sent)


# # Print reverse "Sanjeev is good -> good is Sanjeev"
# name = "sanjeev is a good boy"  
# words = name.split() 
# words.reverse()
# res = ""
# for word in words:
#     res += word + " "
# result = res.strip()
# print(result) #boy good a is sanjeev


# # Check if the given string is palindomeor not
# word = "naman" #This is Palindrome
# reversed_word = word[::-1]
# if word == reversed_word:
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")


# # Check if the given string is palindomeor not
# word = "Naman" #This is not Palindrome due to N is capital
# reversed_word = word[::-1]
# if word == reversed_word:
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")


# # Check if the given string is palindomeor not
# word = "Naman".lower() #This is Palindrome
# reversed_word = word[::-1]
# if word == reversed_word:
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")


# # The word which have max_len
# sentence = "Python is easy language".split()
# max_len = 0
# for word in sentence:
#     print(word) #print updown this sentence


# # The word which have max_len
# sentence = "Python is easy language".split()
# max_len = 0
# for word in sentence:
#     print(len(word)) #count the word's letter and in digit show


# # The word which have max_len
# sentence = "Python is easy language".split()
# max_len = 0
# for word in sentence:
#     if len(word) > max_len:
#         max_len = len(word)
# print(max_len) #8


# # The word which have max_len
# sentence = "Python is easy language".split()
# max_len = 0
# for word in sentence:
#     if len(word) > max_len:
#         max_len = len(word)
# for word in sentence:
#     if len(word) == max_len:
#         print(word) #language 


# # The word which have max_len
# sentence = "Python is easy language".split()
# max_len = 0
# for word in sentence:
#     if len(word) > max_len:
#         max_len = len(word)
# print(max_len) #8
# for word in sentence:
#     if len(word) == max_len:
#         print(word) #language


# print reverse "nohtyP si doog"