# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# *Пример*
#
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
from common_methods import title
title("3 Задайте последовательность чисел. Напишите программу, "
      "которая выведет список неповторяющихся элементов исходной последовательности.")

array = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
answer = []
checked_numbers = []
for i in range(len(array)):
    if array[i] not in checked_numbers:
        checked_numbers.append(array[i])
        counter = True
        for j in range(i + 1, len(array)):
            if array[j] == array[i]:
                counter = False
                break
        if counter:
            answer.append(array[i])


print(answer)
