# https://is35-2020.susu.ru/blog/2020/10/30/algoritmy-sortirovki-na-python/

# def merge(arr, lf, mid, rg):
#     # left, mid; mid + 1, right
#     result = list()
#     first = arr[lf: mid]
#     second = arr[mid: rg]
#     if not first:
#         return second
#     if not second:
#         return first
#     l_first = len(first)
#     l_second = len(second)
#     f_idx = 0
#     s_idx = 0
#     result = []
#     while True:
#         first_elem = first[f_idx]
#         second_elem = second[s_idx]
#         if first_elem < second_elem:
#             result += [first_elem]
#             f_idx += 1
#         else:
#             result += [second_elem]
#             s_idx += 1
#         if f_idx == l_first:
#             ended = 1
#             break
#         if s_idx == l_second:
#             ended = 2
#             break
#     if ended == 2:
#         while f_idx < l_first:
#             result += [first[f_idx]]
#             f_idx += 1
#     else:
#         while s_idx < l_second:
#             result += [second[s_idx]]
#             s_idx += 1
#     return result
#
#
# def merge_sort(arr, lf, rg):
#     if rg - lf <= 1:
#         return
#     mid = (lf + rg) // 2
#     merge_sort(arr, lf, mid)
#     merge_sort(arr, mid, rg)
#     arr[lf: rg] = merge(arr, lf, mid, rg)
#
#
#
#
#
# def test():
#     a = [1, 4, 9, 2, 10, 11]
#     b = merge(a, 0, 3, 6)
#     expected = [1, 2, 4, 9, 10, 11]
#     assert b == expected
#     c = [1, 4, 2, 10, 1, 2]
#     merge_sort(c, 0, 6)
#     expected = [1, 1, 2, 2, 4, 10]
#     assert c == expected


import operator
def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(merge_sort(array))