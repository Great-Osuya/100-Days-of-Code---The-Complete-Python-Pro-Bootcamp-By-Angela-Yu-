# Subscripting using positive numbers starts from the front. So it starts from 'O' for the first number, '1' for the second number, and so on
# Observe the use of '[]' after the string enclosed in "" double quotes
print("Hello"[0])

# Subscripting using negatives starts from the back. So '-1' is the last number, '-2' is second to last, and so on
print("Hello"[-1])

# Strings: any set of characters enclosed by double quotes "". Even numbers
print("Hello")
print("1234 " + "5678") # Plus sign concatenates here because the computer sees this as string and not numbers

# Integers: Whole numbers (No decimal) written without "". The plus sign (+) works like normal here.
print(1234 + 5678) # Notice that we got the answer for the summation '6912'
print(-1234 + 5678)
print(123_456_789_012) # In the place of commas(,), we can use underscores(_) for our own ease

# Float: Decimal Number (Floating point Number)
print(3.142)

#Boolean: True of False. The 'T' and 'F' must be capitalized, without any quotation marks
print(True)
print(False)