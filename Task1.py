# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

from common_methods import title
title("1 Вычислить число π c заданной точностью d")


def next_leibniz(number, mult):
    return mult * 4 / number


d = float(input("Введите число d: "))
multiplier = 1
divider = 1
current_leibniz = 1
answer = 0
n = 0
while abs(current_leibniz) > d / 10:
    # print(f"Итерация №{n}")
    n += 1
    current_leibniz = next_leibniz(divider, multiplier)
    answer += current_leibniz
    divider += 2
    multiplier *= -1
print(answer)
