# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input())
p = int(input())
for x in range(1, 1000):
    y = s - x
    if s == x + y and p == y * x:
        print(x, y)
        break
