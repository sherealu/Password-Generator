#Purpose: To generate a random password
#with numbers and letters

import random #module containing functions like C library

alpha_string = "abcdefghijklmnopqrstuvwsyz"
alpha_array = [x for x in alpha_string] #alpha_array = alpha_string.split() splits by spaces not chars

#request user input for password length
pass_length = int(input("enter password length:"))

password = [0]*pass_length

for n in range(pass_length): #loops through all index values of pass_length
    index_check = random.randint(0,1) #1 = alphabet, 0 = number
    
    if index_check == 1:
        index_alpha = random.randint(0,26)
        password[n] = alpha_array[index_alpha]

    else:
        index_num = str(random.randint(0,10))
        password[n] = index_num

pass_string = "".join(password)
print("Your password is: " + pass_string)