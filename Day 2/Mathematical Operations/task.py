print("My age: " + str(12))

# Mathematical Operations
print(1 + 2) # Addition
print(4 - 3) # Subtraction
print(5 * 6) # Multiplication
print(14 / 7) # Division (ONE SLASH MAKES THE DATA TYPE A FLOATING NUMBER. DECIMAL)
print(14 // 7) # Division (TWO SLASHES MAKE THE DATA TYPE AN INTEGER. NO DECIMAL)
print(2 ** 3) # Exponential (Raise to the power of)

# But you must be careful regarding division, when there is actually meant to be presence of decimal, double slash would 'floor the number to the lowest whole number'.
print(13 // 7) # Notice that the value presented as just '1' without the other decimals (Not the best in this case). It does not even approximate it
print(13 / 7) # Shows the correct allotment of decimals

# Arithmetic Rules in Python follows 'PEMDAS' Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction
# Note that Multiplication and Division are equally important but are prioritized based on position. THe one more leftward gets calculated first

print(3 * 3 + 3 / 3 - 3)

# All Three below give 3 as final answer
print(3 * (3 + 3) / 3 - 3) # The same symbols, just changed the position
print(3 / 3 * 3 + 3 - 3) # The same symbols, just changed the position
print(3 * 3 / 3 + 3 - 3) # The same symbols, just changed the position
