def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# Example usage
file_path = 'your_text_file.txt'
result = count_words(file_path)

if result != -1:
    print(f"The number of words in '{file_path}' is: {result}")
a=input("Enter your name: ")
print(a)

#print("Hello World")
# age=23
# print(age)
# old=True
# print(old)
# if old==False:
#     print("Yes")
# else:
#     print("No")

# #addition of two numbers
# """" This is a example of 
# how to comment multiline"""

# hourly_wages=500
# hours_work=8
# print("Rohan has earned",hourly_wages*hours_work,"Amount working")

# x=int(input("Please enter the amount of days you worked today: "))
# y=int(input("Please unter yout hourly wages "))
# print(x*y)



#problem statement- Get the input from user, counts the number of vowels snd consonents also formats the sentence. 

#taking input from user
# sentence=input("Enter the sentence: ")

# #defining the variables as null 
# vowels= 0
# consonants= 0

# #looping through sentence- counting vowels and consonants
# for char in sentence:
#     if char in 'aeiou':
#         vowels += 1
#     elif char.isalpha():
#         consonants += 1

# #Formatting the sentence
# new_sentence= sentence.capitalize() + '.'

# #Printing the results 

# print("Modified sentence is: ", new_sentence)
# print("Number of vowels : ", vowels)
# print("Numbers of consonants : ", consonants)


