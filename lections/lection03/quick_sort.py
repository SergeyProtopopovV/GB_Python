from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


n = int(input("Enter the number of elements: "))
array = [randint(1, 1000) for i in range(n)]
print(array)
print(quick_sort(array))
