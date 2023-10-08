# переворачивание списка методом reverse()
num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
num.reverse()
print(f"{num[1]}")

# Создание списков
list1 = []
print("Blank list:")
print(list1)

# create list of number
list2 = [1, 2, 3]
print("\nList of number:")
print(list2)

# Creating list of string and number
# using index
list3 = ["Those who lovse Others", "Can you run in the morning?", "Last night was more nice!"]
print("\nList items:")
print(list3[0])
print(list3[2])

# Создание списка с дублирующими значениями
list4 = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6]
print("\nList with the use of number:")
print(list4)

# Creating a list with the mixed values string and numbers
list5 = ["Reno", 5, "Geely", 6, "Mersedess", 9, "Lamborginy"]
print("\nList with the use of Mixed Values:")
print(list5)

# access to the list by index
# Nested lists are accessed using nested indexing.
list6 = [
	'Geniuse',
	'Marck',
	'Power',
	'Alchogol']
print("\nAccessing a element from the list:")
print(list6[0])
print(list6[3])

# nested access list
list7 = [['Radmir', 'Chrome'], ['GeekBreins', 'Place']]
print('Access a element from a Multi-Dimensional list')
print(list7[0][1])
print(list7[1][1])

# negative indexing
list8 = [1, 2, 'Getting', 4, 'Low', 6, 'Steel']
print("Accessing element using negative indexing:")
print(list8[-2])
print(list8[-5])

# Getting the list size("Получения размера списка")с помощью метода "len"
list_a = []
print(len(list_a))
# list with of number
list_b = [10, 20, 30, 40, 50, 60]
print("\n List with of number and getting the list size:")
print(len(list_b))

# Getting input data from a list
# input the list as string
string = input("Enter elements (Space-Separated): ")
lst = string.split()
print('The list is: ', lst)

# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst)
