#Generate a random password using lowercase, uppercase, numbers and symbols

import random

lower_case = "abcdefghijklmnñopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!#$%&/=?¡*"

total_symbols = lower_case + upper_case + numbers + symbols
length_password = 10

password = "".join(random.sample(total_symbols, length_password))
print(password)
