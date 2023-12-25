# Нарезка списка
str = ['G','A', 'R', 'A', 'G', 'M', 'Y', 'V', 'I', 'Z', 'I', 'T', 'C','E']
list_str = str[0]
print('пример 1')
print(list_str,'\n')
print('пример 2, включает в себя от начало до 5 того элемента')
list_str = str[0:5]
print(list_str)
print('пример 3, включает в себя от начала до конца списка')
list_str = str[0:]
print(list_str,'\n')
print('пример 4, включает в себя от начала до конца списка, это тоже самое что и пример 3')
list_str = str[:]
print(list_str,'\n')
# Нарезка списка с отрицательным индексом
print('пример 6: минусовое индекс считается с конца списка и выводит вес список кроме последнего индекса')
list_str = str[:-1]
print(list_str, '\n')
print('пример 7: минусовое индекс считается с конца списка и до 7 го индекса')
list_str = str[-7:-1]
print(list_str,'\n')
print('пример 8: минусовое индекс с значением :: переворачивает вес список')
list_str = str[::-1]
print(list_str,'\n')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_sq =  list[::-1]
for i in list_sq:
   print(f'{i:2.0f}')

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in reversed(lists):
	print(f'{x:<3}', end='\n\t')
	
list2 = ["border", 'sliply']
turn_list = ' ,'.join(list2)
print(turn_list [::-1])