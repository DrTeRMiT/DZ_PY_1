# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def Check_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == ((not x) and (not y) and (not z))}")
#     return (not (x or y or z)) == (not x and not y and not z)


# if (Check_statement(0, 0, 0)
#     and Check_statement(0, 0, 1)
#     and Check_statement(0, 1, 0)
#     and Check_statement(0, 1, 1)
#     and Check_statement(1, 0, 0)
#     and Check_statement(1, 0, 1)
#     and Check_statement(1, 1, 0)
#         and Check_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")


print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == ((not x) and (not y) and (not z)):
                print(x, y, z)
