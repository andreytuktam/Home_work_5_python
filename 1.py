# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_file = open("abv.txt", "w+")
my_file.write("Напишитеабв программу, удаляющую из текстаабв все слова, содержащиеабв")
my_file.close()

my_file = open("abv.txt", "r")
line = my_file.readline()
my_file.close()

print(" ".join(filter(lambda x: "абв" not in x, line.split())))

my_file = open("abv_new.txt", "w+")
my_file.write(line)
my_file.close()