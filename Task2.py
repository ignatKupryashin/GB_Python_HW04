# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# *Пример*
#
# - при N=236     ->        [2, 2, 59]
from common_methods import title

title("2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

question = int(input("Введите число N: "))
answer = []
while question > 1:
    for i in range(2, question + 1):
        if question % i == 0:
            answer.append(i)
            question = int(question / i)
            break
print(answer)
