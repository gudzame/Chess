k = int(input("Введите вертикаль первой фигуры: "))
l = int(input("Введите горизонталь первой фигуры: "))
m = int(input("Введите вертикаль второй фигуры: "))
n = int(input("Введите горизонталь второй фигуры: "))
k2 = k
l2 = l
mod_razn_vert = abs(k - m) #Модуль разности вертикалей
mod_razn_goriz = abs(l - n) #Модуль разности горизонталей
x = mod_razn_vert + mod_razn_goriz
colB = 0 #Чёрный цвет
colW = 0 #Белый цвет
if ((k > 8 or k < 1) and (l > 8 or l < 1) and (m > 8 or m < 1) and (n > 8 or n < 1)) or (k == m and l == n):
    print("Ошибка! Координаты введены некорректно")
else:
    if (((k % 2 == 0 and l % 2 != 0) and (m % 2 == 0 and n % 2 != 0)) or ((k % 2 != 0 and l % 2 == 0) and (m % 2 != 0 and n % 2 == 0)) or ((k % 2 == 0 and l % 2 != 0) and (m % 2 != 0 and n % 2 == 0)) or ((k % 2 != 0 and l % 2 == 0) and (m % 2 == 0 and n % 2 != 0))):
        print("Обе фигуры стоят на чёрных клетках!")
        colB += 1
    elif (((k % 2 == 0 and l % 2 == 0) and (m % 2 == 0 and n % 2 == 0)) or ((k % 2 != 0 and l % 2 != 0) and (m % 2 != 0 and n % 2 != 0)) or ((k % 2 == 0 and l % 2 == 0) and (m % 2 != 0 and n % 2 != 0)) or ((k % 2 != 0 and l % 2 != 0) and (m % 2 == 0 and n % 2 == 0))):
        print("Обе фигуры стоят на белых клетках!")
        colW += 1
    else:
        print("Клетки фигур разного цвета!")

figure = input("Выберите одну из фигур с заглавной буквы: Ладья, Слон, Ферзь, Конь — ")
if figure != "Ладья" and figure != "Слон" and figure != "Ферзь" and figure != "Конь":
    print("Некорректно введено название фигуры!")
else:
    if figure == "Ладья" and (k == m or l == n):
        print(figure + " на клетке " + "(" + str(k) + "," + str(l) + ")" + " угрожает фигуре на клетке " + "(" + str(m) + "," + str(n) + ")")
    elif figure == "Слон" and (mod_razn_vert == mod_razn_goriz):
        print(figure + " на клетке " + "(" + str(k) + "," + str(l) + ")" + " угрожает фигуре на клетке " + "(" + str(m) + "," + str(n) + ")")
    elif figure == "Ферзь" and ((mod_razn_vert == mod_razn_goriz) or (k == m or l == n)):
        print(figure + " на клетке " + "(" + str(k) + "," + str(l) + ")" + " угрожает фигуре на клетке " + "(" + str(m) + "," + str(n) + ")")
    elif figure == "Конь" and ((mod_razn_vert == 1) and (mod_razn_goriz == 2) or (mod_razn_vert == 2) and (mod_razn_goriz == 1)):
        print(figure + " на клетке " + "(" + str(k) + "," + str(l) + ")" + " угрожает фигуре на клетке " + "(" + str(m) + "," + str(n) + ")")
    else:
        print(figure + " на клетке " + "(" + str(k) + "," + str(l) + ")" + " не угрожает фигуре на клетке " + "(" + str(m) + "," + str(n) + ")")
        if figure == "Слон" and colB == 0 and colW == 0:
            print("Слон никак не сможет прийти в клетку " + "(" + str(m) + "," + str(n) + ")" )
        elif figure == "слон":
            if (k + x // 2 <= 8) and (l + x // 2 <= 8):
                k2 += x // 2; l2 += x // 2
            elif (k + x // 2 > 8) and (l + x // 2 > 8):
                k2 -= x // 2; l2 -= x // 2
            elif (k + x // 2 <= 8) and (l + x // 2 > 8):
                k2 += x // 2; l2 -= x // 2
            elif (k + x // 2 > 8) and (l + x // 2 <= 8):
                k2 -= x // 2; l2 += x // 2
            print(figure + " при переходе с клетки " + "(" + str(k) + "," + str(l) + ")" + " на клетку " + "(" + str(k2) + "," + str(l2) + ")" + " угрожает клетке " + "(" + str(m) + "," + str(n) + ")")
        elif figure == "ладья" or figure == "ферзь":
            if k > m:
                k2 -= k - m
            elif k < m:
                k2 += m - k
            print(figure + " при переходе с клетки " + "(" + str(k) + "," + str(l) + ")" + " на клетку " + "(" + str(k2) + "," + str(l) + ")" + " угрожает клетке " + "(" + str(m) + "," + str(n) + ")" + " - первый вариант хода")
            if l > n:
                l2 -= l - n
            elif l < n:
                l2 += n - l
            print(figure + " при переходе с клетки " + "(" + str(k) + "," + str(l) + ")" + " на клетку " + "(" + str(k) + "," + str(l2) + ")" + " угрожает клетке " + "(" + str(m) + "," + str(n) + ")" + " - второй вариант хода")





