# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

msg = input("please provide your message: ")
opt = int(input("1. Code\n2. Decode\n 3.Quit."))
while opt != 3:
    if opt == 1:
        # code
        words = msg.split(" ")
        n_words=[]
        for word in words:
            #characters = "abcdefghijklmnopqrstuvwxyz"  # The collection of characters to pick from
            # random_characters1 = random.sample(characters, 3)
            # random_characters2 = random.sample(characters, 3)
            #pad1 = pad2  = ''
            # pad1 = ''.join(random_characters1)
            # pad2 = ''.join(random_characters2)
            pad1 = random.choices(string.ascii_lowercase,k = 3)
            pad2 = random.choices(string.ascii_lowercase,k = 3)
            word = ''.join(pad1) + word[1:] + word[0] + ''.join(pad2) if len(word) >= 3 else word[::-1]
            n_words.append(word)
        c_msg = " ".join(n_words)
        print(f"Coded messge is     :{c_msg}")
    elif opt==2:
        #  Decode
        words = c_msg.split(" ")
        n_words =[]
        for word in words:
            word = word[::-1] if len(word) < 3 else word[-4] + word[3:-4]
            n_words.append(word)
        d_msg = " ".join(n_words)
        print(f"De-oded messge is   :{d_msg}")
    else:
        print(f"You have entered incorrect option: {opt}, please enter value 1 or 2 or 3.")
    opt = int(input("1. Code\n2. Decode\n 3.Quit."))


