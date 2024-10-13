#Purpose: To generate a random password
#with numbers and letters

import random 

alpha_string = "abcdefghijklmnopqrstuvwsyz"
alpha_array = [x for x in alpha_string] #alpha_array = alpha_string.split() splits by spaces not chars

#request user input for password length
print("Enter password length below:")
pass_length = input("enter password length:")

n = 0

for n in 26:
    index = random.randrange(0,26)


print("Your password is: " + password) #initiate password array
