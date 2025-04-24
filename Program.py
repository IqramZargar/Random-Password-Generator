import random
#import random used for genrating a single value out of many values from letters, digits, punctuation.
import string
#import string used for generating all values from letters, digits, punctuations.

random_password = ""
#Assigning a variable with empty string.
print("------------------WELCOME TO RANDOM PASSWORD GENERATOR-------------------------- ")
#simple print.
print("-> THE PASSWORD THAT WILL BE GENERATED WILL CONTAIN RANDOM COMBINATION OF (A-Z),(a-z),(0-9), AND SPECIAL CHARECTERS.")
#simple print.
n = int(input("-> WHAT SHOULD BE THE LENTH OF PASSWORD :- "))
#Getting input from user as to get the length of the password user wants to generate.
char_values =  string.digits + string.ascii_letters + string.punctuation
#stored every value of digits, letters, punctuation values in char_values
for i in range(n):
#using for-loop and running it till i reaches length of n.    
    val = random.choice(char_values)
#used random.choice for choosing random value form char_values    
    random_password += val
#each random value generated above stored in random_password till it meets the desired lenth of password user wanted.    
print("BINGO! YOUR RANDOM PASSWORD HAS SUCCESSFULLY GENERATED :- ",random_password)
#Finished the generation of random password.
#You can simply copy the password and use it wherever you want.

