# full_name  = "Sanjeev Kumar"
# print(full_name)


# print(ord('a')) #print "a value is 97"


# #My name is Sanjeev print
# name = "Sanjeev"
# print(f"My name is " +name)


# # Kumar sanjeev print
# first_name = "sanjeev"
# last_name = "Kumar"
# print("{1} {0}".format(first_name,last_name))



# #Print the word max-length , here is pineapple max-length "['Pineapple', 'is', 'tastey.', 'Banana', 'is', 'less', 'tastey.']"
# sentence = "Pineapple is tastey. Banana is less tastey.".split()
# print(sentence)

# #Print the word max-length , here is pineapple max-length  "9 is print"
# sentence = "Pineapple is tastey. Banana is less tastey.".split()
# max_len = 0
# for word in sentence:
#     if len(word) > max_len:
#         max_len = len(word)
# print(max_len)


# # Reverse the Words "Python is Good -> nohtyP si dooG"
# sen = "Python is Good".split() # ['Python', 'is', 'Good']
# print(sen)


# # Reverse the Words "Python is Good -> nohtyP si dooG"
# sen = "Python is Good".split()
# sen.reverse() #['Good', 'is', 'Python']
# print(sen)


# # Reverse the Words "Python is Good -> Good is Python"
# sen = "Python is Good".split()
# reverse_sen = ' '.join(sen[::-1]) #Good is Python
# print(reverse_sen)


# # Reverse the Words "Python is Good -> nohtyP si dooG"
# sen = "Python is Good".split()
# reverse_sen = " "
# for word in sen:
#     print(word[::-1]) #up-down me dega or reverse me bhi


# # Reverse the Words "Python is Good -> nohtyP si dooG"
sen = "Python is Good".split()
reverse_sen = ""
for word in sen:
    reverse_sen += word[::-1] + " "
print(len(reverse_sen)) #16 


# # Reverse the Words "Python is Good -> nohtyP si dooG"
sen = "Python is Good".split()
reverse_sen = " "
for word in sen:
    reverse_sen += word[::-1] + " "
print(len(reverse_sen.strip())) #14 


# # Reverse the Words "Python is Good -> nohtyP si dooG"
# sen = "Python is Good".split()
# reverse_sen = " "
# for word in sen:
#     reverse_sen += word[::-1] + " "
# result = reverse_sen.strip()
# print(len(result)) #14


# #Ask user to input their and that name consists of string or alphabets. If the name is consist.
# #Alphabets print the name otherwise ask user to enter a valid name.
# name = input("Enter your name: ")
# if name.isalpha():
#     print(name)
# else:
#     print("Enter your valid name: ")

# #True print
# sentence = "Python3 is better version then the Python1"
# sent = '1'
# s = sent.isdigit()
# print(s)


#False print
# sentence = "Python3 is better version then the Python1"
# sent = '2'
# s = sent.isdigit()
# print(s)



# #Print up-down letter of this sentence
# sentence = "Python3 is better version then the Python1"
# for c in sentence:
#     print(c) 



# #Print up-down words of this sentence
# sentence = "Python3 is better version then the Python1"
# for c in sentence.split():
#     print(c) 


# #print para
# para = """ Sometimes, you want Python to interpret a character or sequence of characters within a string differently. This may occur in one of two ways. You may want to:

# Apply special meaning to characters
# Suppress special character meaning """
# print(para)


# #Count the digit which are into the given sentence 3,1
# sentence = "Python3 is more better than Python1"


# # ['v', 'e', 'e', 'j', 'n', 'a', 's'] this will be printed
# s = list("sanjeev")
# left = 0
# right = len(s) - 1
# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# print(s)



# # veejnas print
# s = list("sanjeev")
# left = 0
# right = len(s) - 1
# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# reversed_name = ''.join(s) 
# print(reversed_name)



