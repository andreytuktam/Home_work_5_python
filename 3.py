# Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:
#    |   | 0
# -----------    
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

from random import randint


pole = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
print("|".join(pole[0]))
print("-----------")
print("|".join(pole[1]))
print("-----------")
print("|".join(pole[2]))
s = 1
p = 0
k = randint(0, 1)
print(s)
flag = True
while flag == True:
    if k == 0:
        x = (int(input('игрок #1 введи номер строки 1-3: ')) - 1)
        y = (int(input('игрок #1 введи номер столбца 1-3: ')) - 1)
        if pole[x][y] != " 1 ":
            pole[x][y] = " 0 "
        else:
            print("эта ячейка занята, перезапусти программу!")
            flag = False
        print("|".join(pole[0]))
        print("-----------")
        print("|".join(pole[1]))
        print("-----------")
        print("|".join(pole[2]))
        k = k + 1
        s += 1
        print(s)
        if pole[0][0] == pole[1][0] == pole[2][0] == " 0 " or pole[0][1] == pole[1][1] == pole[2][1] == " 0 " or\
            pole[0][2] == pole[1][2] == pole[2][2] == " 0 " or pole[0][0] == pole[0][1] == pole[0][2] == " 0 " or\
            pole[1][0] == pole[1][1] == pole[1][2] == " 0 " or pole[2][0] == pole[2][1] == pole[2][2] == " 0 " or\
            pole[0][0] == pole[1][1] == pole[2][2] == " 0 " or pole[0][2] == pole[1][1] == pole[2][0] == " 0 ":
            print('игрок #1 победил')
            p += 1
            if p == 2:
                flag = False
        
        if s == 10:
            flag = False
    if k == 1 and flag != False:
        x1 = (int(input('игрок #2 введи номер строки 1-3: ')) - 1)
        y1 = (int(input('игрок #2 введи номер столбца 1-3: ')) - 1)
        if pole[x1][y1] != " 0 ":
            pole[x1][y1] = " 1 "
        else:
            print("эта ячейка занята, перезапусти программу!")
            flag = False  
        print("|".join(pole[0]))
        print("-----------")
        print("|".join(pole[1]))
        print("-----------")
        print("|".join(pole[2]))
        k = k - 1
        s += 1
        print(s)
        if pole[0][0] == pole[1][0] == pole[2][0] == " 1 " or pole[0][1] == pole[1][1] == pole[2][1] == " 1 " or\
            pole[0][2] == pole[1][2] == pole[2][2] == " 1 " or pole[0][0] == pole[0][1] == pole[0][2] == " 1 " or\
            pole[1][0] == pole[1][1] == pole[1][2] == " 1 " or pole[2][0] == pole[2][1] == pole[2][2] == " 1 " or\
            pole[0][0] == pole[1][1] == pole[2][2] == " 1 " or pole[0][2] == pole[1][1] == pole[2][0] == " 1 ":
            print('игрок #2 победил')
            p += 1
            if p == 2:
                flag = False 
            
        if s == 10:
            flag = False  
if p == 2:
    print("ничья!")
            
                
                