import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + symbols
length = 16
password = "".join(random.sample(all,length))

print(password)