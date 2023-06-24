import random
passwordlength=int(input("enter the length of the password"))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#!$%^&*()_?"
p="".join(random.sample(s,passwordlength))
print(p)
 