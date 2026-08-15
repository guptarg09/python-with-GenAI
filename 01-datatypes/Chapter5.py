import sys   # sys → interact with Python's interpreter/system information.
from fractions import Fraction  # Fraction → exact rational/fraction arithmetic.
from decimal import Decimal # Decimal → is useful when you need exact decimal arithmetic.

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(sys.float_info)  # -> This gives information about Python's floating-point implementation.


# Because Python's float uses IEEE 754 double-precision binary floating point. Decimal numbers such as 95.49 and 0.01 generally cannot be represented exactly in binary.

# So internally, Python stores very close approximations:

# 95.5   → approximately 95.500000000000...
# 95.49  → approximately 95.489999999999...