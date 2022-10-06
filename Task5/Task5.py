# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

with open("first_expression.txt", "r") as file:
    first_expression = file.read()
with open("second_expression.txt", "r") as file:
    second_expression = file.read()

first_expression = str.replace(first_expression, "- ", "+ -").split()
second_expression = str.replace(second_expression, "- ", "+ -").split()

first_expression = list(filter(lambda x: x != "+" and x != "=" and x != "0", first_expression))

# def to_tuple(array):


print(first_expression)




# print(second_expression)
