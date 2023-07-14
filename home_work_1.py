# .Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны 
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a_side = int(input("Введите значение длинны стороны А = "))
b_side = int(input("Введите значение длинны стороны В = "))
c_side = int(input("Введите значение длинны стороны С = "))

if a_side + b_side > c_side and b_side + c_side > a_side and c_side + a_side > b_side:
    if a_side == b_side and b_side == c_side:
        print("Равносторонний треугольник")
    elif a_side == b_side or b_side == c_side or a_side == c_side:
        print("Равнобедренный треугольник")
    else:
        print("Разностороннийтреугольник")
else:
    print("не треугольник")

# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки:
#  “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


max = 100000
min = 0
number = None
while (number == None or number < min or number > max):
    number = int(input("введите целое число больше 0 и меньше 100 000 ="))
count = 0
for i in range(2, number - 1, 1):
    if number % i == 0:
        count += 1

if count > 0:
    print(f"число ", number, "составное")
else:
     print(f"число ", number, "простое")