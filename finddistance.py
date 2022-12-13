# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
x1 = int(input('X= '))
y1 = int(input('Y= '))

print('Введите координаты точки B')
x2 = int(input('X= '))
y2 = int(input('Y= '))

import math

def Distance(a1, a2, b1, b2):
    dist = float(math.sqrt((a1-a2)*(a1-a2)+(b1-b2)*(b1-b2)))
    return dist

distance = Distance(x1,x2,y1,y2)
print(distance)