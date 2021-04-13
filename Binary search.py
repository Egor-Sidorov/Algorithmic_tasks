

def binary_search(arr_sorted, elem_needed, low, high):
    pivot_index = (high+low) // 2
    if arr_sorted[pivot_index] != elem_needed and high <= low :
        return -1
    elif arr_sorted[pivot_index] == elem_needed:
        return pivot_index + 1
    elif arr_sorted[pivot_index] > elem_needed:
        new_high = pivot_index - 1
        return binary_search(arr_sorted, elem_needed, low, new_high)
    elif arr_sorted[pivot_index] < elem_needed:
        new_low = pivot_index + 1
        return binary_search(arr_sorted, elem_needed, new_low, high)


arr_1_s = list(map(int, input().split()))
arr_2_n = list(map(int, input().split()))
arr_sorted_leng = arr_1_s.pop(0)
arr_needed_leng = arr_2_n.pop(0)
arr_founded_indexes = []

lo = 0
hi = arr_sorted_leng - 1

for i in range(arr_needed_leng):
    element_n = arr_2_n[i]
    arr_founded_indexes.append(binary_search(arr_1_s, element_n, lo, hi))

print(*arr_founded_indexes)

