#import the necessary modules!
import random
import string

print('Hello, Welcome to Password generator!!!')

#taking input for the length of password
length = int(input('\nEnter the length of password (max 94): '))                      

#defining the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combining the data
new = lower + upper + num + symbols

#using random 
var = random.sample(new,length)

#creating the password 
password = "".join(var)

#printing the password
print(password)