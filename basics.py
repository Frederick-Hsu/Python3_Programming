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