# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


my_file = open("rle.txt", "w+")
my_file.write("aaaannnpppppllluuu")
my_file.close()

my_file = open("rle.txt", "r")
stroka = my_file.readline()
my_file.close()

stroka = [char for char in stroka]
stroka_kod = []
print(stroka)
m = 0
k = 0

for i in range(0, len(stroka) - 1):
    if stroka[i] == stroka[i+1]:
        m += 1
    else:
        
        stroka_kod.append(m + 1)
        stroka_kod.append(stroka[i - 1])
        k += m + 1
        m = 0
      
stroka_kod.append(len(stroka) - k)
stroka_kod.append(stroka[len(stroka) - 1])

stroka_kod_itog = []
for i in stroka_kod:
    i = str(i)
    stroka_kod_itog.append(i)
stroka_kod_itog = "".join(stroka_kod_itog)
print(stroka_kod_itog)

stroka_kod_itog = [char for char in stroka]
stroka_kod_itog_2 = []

for i in stroka_kod_itog:
    i = str(i)
    stroka_kod_itog_2.append(i)
stroka_kod_itog_2 = "".join(stroka_kod_itog_2)
print(stroka_kod_itog_2)

my_file = open("rle_itog.txt", "w+")
my_file.write(stroka_kod_itog_2)
my_file.close()
