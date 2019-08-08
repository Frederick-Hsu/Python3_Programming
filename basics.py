# -*- coding: utf-8 -*-
#
# File name     : basics.py
# Description   : Learn the basics of Python3 programming.
# Creator       : Frederique Hsu
# Creation date : Wed.  07 Aug. 2019
# Copyright(C)  2019    ALl rights reserved.
#

print(dir())   # return the built-in properties list of Python
print(dir(__builtins__))

print("\n====================================================\n")

# Integral type
decimal_integral = 145908635
binary_integral = 0b101110010010111101101
octal_integral = 0o7636054
hex_integral = 0xF95A50CEBD056E

print(decimal_integral)
print(binary_integral)
print(octal_integral)
print(hex_integral)

print(decimal_integral + octal_integral)
print(decimal_integral - octal_integral)
print(decimal_integral * octal_integral)
print(decimal_integral / octal_integral)
print(decimal_integral // octal_integral)
print(decimal_integral % octal_integral)
print(binary_integral ** 3)
print(divmod(decimal_integral, octal_integral))
print(pow(binary_integral, 3))
print(pow(binary_integral, 3, octal_integral))  # pow(x, y, z) = x^y % z
print(round(decimal_integral/octal_integral, 8))

print("\n====================================================\n")

# 使用数据类型创建对象
x = int()   # 1. 不使用参数调用数据类型函数
print(x)

year = 2019
this_year = int(year)    # 2. 使用一个参数调用数据类型函数
print("this year is : ", this_year)
print("bin(this_year) = ", bin(this_year))
print("hex(this_year) = ", hex(this_year))
print("oct(this_year) = ", oct(this_year))

number = int("A4", 16)  # 3. 给定两个或多个参数，但不是所有数据类型都支持。
print("number = ", number)
print("hex(number) = ", hex(number))

print("\n====================================================\n")

# bitwise operation
operand_x = 0b1011001111110110
operand_y = 0b1111100111010011
print("operand_x = ", bin(operand_x))
print("operand_y = ", bin(operand_y))
print("operand_x & operand_y = ", bin(operand_x & operand_y))   # AND
print("operand_x | operand_y = ", bin(operand_x | operand_y))   # OR
print("operand_x ^ operand_y = ", bin(operand_x ^ operand_y))   # XOR
print("operand_x << 5 = ", bin(operand_x << 5))     # Bitwise Left Shift
print("operand_y >> 5 = ", bin(operand_y >> 5))     # Bitwise Right Shift
print("~operand_x = ", bin(~operand_x))                # Bitwise NOT

print("\n====================================================\n")

# Float type
import decimal
salutary = 0.0, 5.4, -2.5, 8.9e-6
print("salutary = ", salutary)

precise_pi = decimal.Decimal(3.14159267)
print(precise_pi)

import sys
def equal_float(a, b):
    return (abs(a - b) <= sys.float_info.epsilon)   # epsilon是机器可以区分出两个浮点数的最小区别

# Display the detailed information about the function, class you want to query
help(sys.float_info.epsilon)

float_number = 14.25
hex_float_string = float_number.hex()
print("\nConvert float number ", float_number, " to hex string : ", hex_float_string)
print("\nConvert hex float string ", hex_float_string, " back to float number : ", float.fromhex(hex_float_string))
print("\nExpress the float number ", float_number, " as integer ratio : ", float.as_integer_ratio(float_number))

import math
circle_area = math.pi * pow(5, 2)
print("\nThe area of a circle with radius 5 is : ", circle_area)
print("\nA right-angled triangle, hook is 5, stock is 12, \naccording to the Pythagoras theory, its string is : ", math.hypot(5, 12))
print("\nReturning the fractional and integer parts of ", 13.732, ", they are : ", math.modf(13.732))