import string
import pyperclip
import random
import os
passwordKey = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
random.shuffle(passwordKey)
plen = int(input('Enter Your Password Length Between 1 To 94 : '))
password = ''.join(passwordKey[:plen])
pyperclip.copy(password)
print(f'Your Password Is {password} And Is Copied In Your Clipboard\n')
print('Press Any Key To Exit...')
os.system('pause > nul')
