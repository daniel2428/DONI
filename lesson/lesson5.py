# Big Натация
#Git
#Повторение тем
from unittest.mock import right

#o(1) -Констанкная время
#Алгоритм работает за фиксированное время,
# Независимо от размера входных данных

# Доступ к элементу списка по индексу - 0(1)
lst = [0,1,2,3,4,5,6,7,8,9]
def get_element_by_index(lst, index):
    return lst[index]
print(get_element_by_index(lst=lst, index=4))


# O(log n) -  Логарифмическое время
# Часто втречается в алгоритмах, используется
#деление входных данных на части (например. бинарный список)

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return -1

print(binary_search(lst,9))












lst3 = [9,2,5,1,5,2,8,7,45]
print(lst3.sort())

#O(n²) - Квадратное время
#Обычно встречается в алгоритмах с двумя



def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubble_sort(lst=lst3)
print(lst3)