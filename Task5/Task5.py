# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

with open("first_expression.txt", "r") as file:
    first_expression = file.read()
with open("second_expression.txt", "r") as file:
    second_expression = file.read()


def to_tuple(my_string):
    my_string = str.replace(my_string, "- ", "+ -").split()
    my_string = list(filter(lambda x: x != "+" and x != "=" and x != "0", my_string))
    for i in range(len(my_string)):
        my_string[i] = my_string[i].split("*")
    return my_string


first_expression = to_tuple(first_expression)
second_expression = to_tuple(second_expression)

sum_expression = first_expression + second_expression
for i in range (len(sum_expression)):
    if len(sum_expression[i]) == 1:
        sum_expression[i] = [sum_expression[i].pop(0), "X^0"]
cash = []
answer = []

print(sum_expression)

for i in range(len(sum_expression)):
    key = sum_expression[i][1]
    if key not in cash:
        cash.append(key)
        current_sum = int(sum_expression[i][0])
        for j in range(i + 1, len(sum_expression)):
                if key == sum_expression[j][1]:
                    current_sum += int(sum_expression[j][0])
        answer.append([current_sum, key])


for i in range(len(answer)):
    answer[i] = str(answer[i][0]) + "*" + str(answer[i][1])
answer = str(" + ".join(answer))

answer = str.replace(answer, "+ -", "- ")
answer = str.replace(answer, "*X^0", "")
answer = str.replace(answer, "1*", "")

answer += " = 0"

with open("answer.txt", "w") as file:
    file.write(answer)





# print(second_expression)
