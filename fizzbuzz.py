import sys
 
# for i in range(100):
#     if i % 3 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)
        

# x = 1
# while x!=0 :
    
#     x = int(input("Enter a number: "))   
#     if x==0:
#         break
#     if x % 2 == 0:
#       print("Even")
#     elif x % 2 != 0:
#      print("Odd")


#Write a function that takes two numbers as input and returns the maximum of the two.


# def big():
#     one = int(input("enter a number: "))
#     two = int(input("enter again: "))
#     print(max(one,two))

# big()




#Write a function that takes a string as input and returns "Long" if the 
# length of the string is greater than 10 characters, and "Short" otherwise.

# def sentence_size():
#     enter = str(input("enter a sentence: "))
#     if len(enter) >= 10:
#         print("Long")
#     else:
#         print("short")
        
# sentence_size()


# Write a Python program that takes a sentence as input and generates a list containing the 
# lengths of each word in the sentence. Use list comprehension for this task.


# def word_lengths(sentence):
#     return [len(word) for word in sentence.split()]

# sentence =input( "Write a a sentence: ")
# print(word_lengths(sentence)) 




# Write a function that takes a list of numbers as input 
# and returns the sum of all positive numbers in the list.



      

def positive_sum(numbers):
    return sum(i for i in numbers if i > 0)

numbers = [1, -2, 3]
print(positive_sum(numbers))  