
def data_count(t, matrix):
    numbers = []
    max_point = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)

    for i, value in enumerate(numbers):
        if value == 0:
            continue
        if int(value) <= t:
            max_point += 1
    return max_point


def valid_keys(keys):
    if not keys.isnumeric():
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 1 до 5 включительно.')
        sys.exit(1)
    elif 5 < int(keys) or int(keys) < 1:
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 1 до 5 включительно.')
        sys.exit(1)


def valid_matrix(matrix):
    pat = re.compile(r"[1-9.]+")
    if re.fullmatch(pat, matrix) is None:
        print(f'Необходимо ввести '
              f'число от 1 до 9 включительно, или точку.')
        sys.exit(1)


def main():
    len_array = input()
    valid_len_array(n)

    elem_find = input()
    valid_elem_find(k)

    array = list(map(int, input().split()))
    valid_array(array)

    #print(data_count(keys_int, matrix))


if __name__ == '__main__':
    main()


# _____________________________________________________________

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
arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
broken_search(arr, 5)