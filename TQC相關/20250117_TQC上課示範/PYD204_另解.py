# TODO
a = int(input())
b = int(input())
sign = input()

if sign == "+":
    result = a + b
elif sign == "-":
    result = a - b
elif sign == "*":
    result = a * b
elif sign == "/":
    result = a / b
elif sign == "//":
    result = a // b
elif sign == "%":
    result = a % b
elif sign == "**":
    result = a ** b
print(result)