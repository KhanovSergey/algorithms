import sys


def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        if nums[middle] == target:
            return middle
        if nums[left_border] <= nums[middle]:
            if nums[left_border] <= target < nums[middle]:
                right_border = middle - 1
            else:
                left_border = middle + 1
        else:
            if nums[middle] < target <= nums[right_border]:
                left_border = middle + 1
            else:
                right_border = middle - 1
    return -1


def valid_len_array(keys):
    l_arrey = len(array)
    if not keys.isnumeric():
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 0 до 10000 включительно.')
        sys.exit(1)
    elif 0 > int(keys) or int(keys) > 10000:
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 0 до 10000 включительно.')
        sys.exit(1)
    elif int(keys) != l_arrey:
        print(f'Вы ввели {keys[0]}, не соответствующий'
              f' длине массива {l_arrey}')
        sys.exit(1)


def valid_elem_find(elem_find):
    if not elem_find.isnumeric():
        print(f'Вы ввели {elem_find[0]}, требуется ввести число'
              f' от 0 до 10000 включительно.')
        sys.exit(1)
    elif 0 > int(elem_find) or int(elem_find) > 10000:
        print(f'Вы ввели {elem_find[0]}, требуется ввести число'
              f' от 0 до 10000 включительно.')
        sys.exit(1)


def main():
    valid_len_array(len_array)
    valid_elem_find(elem_find)

    return broken_search(array, int(elem_find))


if __name__ == '__main__':
    len_array = input()
    elem_find = input()
    array = list(map(int, input().split()))
    print(main())
