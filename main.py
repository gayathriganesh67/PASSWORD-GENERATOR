import random
import string
lengthofpassword=int(input("Enter the length of password:"))
chars =string.ascii_letters
chars +=string.digits
chars +=string.punctuation
password=""
for i in range(lengthofpassword):
  characterr=random.choice(chars)
  password+=characterr
print("The password is:",password)