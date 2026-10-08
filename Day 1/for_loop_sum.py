'''
s = '123456789'
Given string s,
Write a python program calculate sum of the digits.
use: for loop.
'''
s = '123456789'
sum_digits = 0
for char in s:
    sum_digits += int(char)
print(f"Sum of digits in {s} is: {sum_digits}")