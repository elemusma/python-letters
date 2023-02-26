# import os
# with open('/Users/efrainlemus-martinez/Desktop/data.txt') as file:
# /Users/efrainlemus-martinez/Desktop/Python-Course
# with open('../../data.txt') as file:
#     contents = file.read()
#     print(contents)

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# os.getcwd()
ready_to_send = []
# /Users/efrainlemus-martinez/Desktop/Python-Course/Day-024/Mail Merge Project Start/Input/Names
# /Users/efrainlemus-martinez/Desktop/Python-Course/Day-024/Mail Merge Project Start
with open('Input/Names/invited_names.txt') as names:
# with open('text.txt') as names:
    names_in_list = names.readlines()

for name in names_in_list:
    name = name.strip()
    # name = name.replace('\n', '')
    with open('Input/Letters/starting_letter.txt', mode='r') as letter:
        letter_read = letter.read().replace('[name]', name)
        ready_to_send.append(letter_read)
    
    with open(f'Output/ReadyToSend/{name}.txt', 'w') as letter_send:
        letter_send.write(letter_read)

# print(ready_to_send)
# for letter in ready_to_send:
#     new_letter = open()
#     print(letter)

    # print(letter_read)

# print("hello world")
# letter = open('Input/Letters/starting_letter.txt', mode='r')
# letter_content = letter.read()
# letter_content.replace('[name]', 'Name02')
# print(letter_content)