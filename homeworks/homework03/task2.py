# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 2, 3, 3, 5]
k = 3

minimum, element = k, k

for i in list_1:
    if abs(i - k) <= minimum:
        minimum, element = abs(i - k), i

print(element)
