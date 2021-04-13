"""
В первой строке задано два целых числа  500001≤n≤50000 и  500001≤m≤50000
— количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа ai и bi — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек.
Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

import sys


def quick_sort_partition(arr, low, high):
    if low >= high:
        return arr
    else:
        random_index = (low + high) // 2
        arr[low], arr[random_index] = arr[random_index], arr[low]
        pivot_index = low + 1
        equals_counter = 0
        for i in range(low + 1, high + 1):
            if arr[i] < arr[low]:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
                arr[pivot_index - equals_counter], arr[pivot_index] = arr[pivot_index], arr[
                    pivot_index - equals_counter]
                pivot_index += 1
            elif arr[i] == arr[low]:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

                equals_counter += 1
                pivot_index += 1
        arr[low], arr[pivot_index - equals_counter - 1] = arr[pivot_index - equals_counter - 1], arr[low]
        equals_counter += 1

        less_high = pivot_index - equals_counter - 1
        greater_low = pivot_index
        arr = quick_sort_partition(arr, low, less_high)
        arr = quick_sort_partition(arr, greater_low, high)

        return arr


def binary_search_less(arr, elem_needed, low, high):
    if low > high:
        return low
    else:
        mid = (high + low) // 2
        if elem_needed < arr[mid]:
            high = mid - 1
            return binary_search_less(arr, elem_needed, low, high)
        elif elem_needed > arr[mid]:
            low = mid + 1
            return binary_search_less(arr, elem_needed, low, high)
        else:
            counter = 0
            for i in range(mid, high + 1):
                if arr[i] == elem_needed:
                    counter += 1
                else:
                    break
            return mid + counter


def binary_search_less_strictly(arr, elem_needed, low, high):
    if low > high:
        return low
    else:
        mid = (high + low) // 2
        if elem_needed < arr[mid]:
            high = mid - 1
            return binary_search_less_strictly(arr, elem_needed, low, high)
        elif elem_needed > arr[mid]:
            low = mid + 1
            return binary_search_less_strictly(arr, elem_needed, low, high)
        else:
            counter = 0
            for i in range(0, mid - low + 1):
                if arr[mid - i] == elem_needed:
                    counter += 1
                else:
                    break
            return mid + 1 - counter


segments, points = map(int, input().split())
a_ends = [0] * segments
b_ends = [0] * segments
for segment in range(segments):
    a_ends[segment], b_ends[segment] = map(int, input().split())

a_ends_sorted = sorted(a_ends)
b_ends_sorted = sorted(b_ends)

points_arr = sys.stdin.read().split()
points_n_segments = []

for i in range(points):
    c = int(points_arr[i])
    len_a = binary_search_less(a_ends_sorted, c, 0, segments - 1)
    len_b = binary_search_less_strictly(b_ends_sorted, c, 0, segments - 1)
    points_n_segments.append(len_a - len_b)

print(*points_n_segments)
