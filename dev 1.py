# name = ("Python")
# print (name.lower())/ upper


# for i in  'Saikal':
#     print(i , end="")


# name = 'Python'
# print(len(name))#длина строки

# name = "Python"
# print(name[2:5:2])

#
# name = "Python"
# print(name[::-1])# наоборот читает
#
#
# name = "Python devevlnksdlnv knlsdnlf"
# print(name.count(' '))#пробел
#
#
# name = "python devevlnksdlnv pylsdnlf"
# print(name.replace('py', "Asan")) #замена




name = "Saikal python"

print(len(name))                # len считает симвалы

for i in name:
    print(i, end=' ')           # i, end=' ' печатает с пробелами
print()                         # t u m a r   p y t h o n

print(name[1:4:1])              # 'uma' start:stop:step, срез строки

print(name[::-1])               # 'nohtyp ramut', срез с шагом -1 — переворачивает строку

print(name.count(' '))          # 1, считает сколька пробелов в строке

print(name.replace('py','Asan'))  # 'saikal Asanthon'

print(repr(name[5]), name[5].isalpha())   # ' ' False проверяет символ является ли буквой,
                                                    # если это пробел или цифра вернёт False

print(name.index('h'))          # 9 проверяет в каком индексе символ
                                     # Если символ не найден — бросает ValueError.

print(name[5].isdigit())        # False. проверяет является ли символ цифрой
                                     # если пробела или буквы вернёт False.


