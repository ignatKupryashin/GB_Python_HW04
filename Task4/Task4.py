# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input("Введите коэффициент k: "))
array = []
for i in range(k + 1):
    random_number = int(random.randrange(-10, 10))
    if random_number == 0:
        continue
    if random_number > 0:
        if len(array) > 0:
            array.append("+")
    else:
        array.append("-")
    if k - i > 0:
        array.append(str(f"{abs(random_number)}*X^{k - i}"))
    else:
        array.append(str(abs(random_number)))

array.append("= 0")

with open('answer.txt', 'a') as file:
    file.write(" ".join(array) + "\n")

