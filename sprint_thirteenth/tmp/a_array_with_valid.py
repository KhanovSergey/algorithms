"""
ID 68741067
Code edits after the first review.
"""
import sys


def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        if nums[middle] == target:
            return middle
        if nums[left_border] > nums[middle]:
            if nums[middle] < target <= nums[right_border]:
                left_border = middle + 1
            else:
                right_border = middle - 1
        else:
            if nums[left_border] <= target < nums[middle]:
                right_border = middle - 1
            else:
                left_border = middle + 1
    return -1


def valid_len_array(keys):
    if not keys.isnumeric():
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 0 до 10000 включительно.')
        sys.exit(1)
    elif 0 > int(keys) or int(keys) > 10000:
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 0 до 10 000 включительно.')
        sys.exit(1)


def valid_elem_find(elem_find):
    if not elem_find.isnumeric():
        print(f'Вы ввели {elem_find[0]}, требуется ввести число'
              f' от 0 до 10 000 включительно.')
        sys.exit(1)
    elif 0 > int(elem_find) or int(elem_find) > 10000:
        print(f'Вы ввели {elem_find[0]}, требуется ввести число'
              f' от 0 до 10 000 включительно.')
        sys.exit(1)


def valid_array(array, len_array):
    joi_array = str("".join(array))
    l_array = len(array)
    if not joi_array.isnumeric():
        print("В строке ввели одно или более значений не int!")
        sys.exit(1)

    elif int(len_array) != l_array:
        print(f'Вы ввели {len_array[0]}, не соответствующий'
              f' длине массива {l_array}')
        sys.exit(1)


if __name__ == '__main__':
    len_array = input()
    valid_len_array(len_array)

    elem_find = input()
    valid_elem_find(elem_find)

    array = input().strip().split()
    valid_array(array, len_array)

    array = list(map(int, array))
    print(broken_search(array, int(elem_find)))
