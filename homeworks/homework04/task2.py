# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:
# 19

max_berries = arr[0]
for i in range(-2, len(arr) - 2):
    summ = arr[i] + arr[i + 1] + arr[i + 2]
    if summ > max_berries:
        max_berries = summ
print(max_berries)

print(max([(arr[i] + arr[i + 1] + arr[i + 2]) for i in range(-2, len(arr) - 2)]))

