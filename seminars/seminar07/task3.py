# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.

# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same

# def same_by(charc, obj) -> bool:
#     return len(set(map(charc, obj))) <= 1
#
#
# values = [2,3,4,6,8]
#
# print(same_by(lambda x: x % 2 == 0, values))
#
#
# print(list(map(lambda x: str(x), values)))

def same_by(characteristic, elements):
    obj = map(characteristic, elements)
    return all(obj) or not any(obj)


elements1 = [2, 4, 6, 8, 10]  # -> True
elements2 = [1, 2, 3, 4, 5]  # -> False
elements3 = [1, 3, 5, 7, 9]  # -> True
elements4 = []  # -> True

print(elements1, same_by(lambda x: x % 2 == 0, elements1))
print(elements2, same_by(lambda x: x % 2 == 0, elements2))
print(elements3, same_by(lambda x: x % 2 == 0, elements3))
print(elements4, same_by(lambda x: x % 2 == 0, elements4))
