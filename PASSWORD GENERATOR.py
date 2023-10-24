# Creating a password generator
import random
print('Welcome To Your Password Generator')
chars = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,0123456789'

number = input('Numbers of password to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nHere are your passwords: ')

for password in range(number):
    passwords: str = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
