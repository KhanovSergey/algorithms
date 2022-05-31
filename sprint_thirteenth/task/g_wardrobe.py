def counting_sort(array):
    COUNT_COLOR = 3
    count_values = [0] * COUNT_COLOR
    for value in array:
        count_values[value] += 1

    index = 0
    for value in range(COUNT_COLOR):
        for _ in range(count_values[value]):
            array[index] = value
            index += 1
    return array


if __name__ == '__main__':
    count_item = int(input())
    sequen = list(map(int, input().split()))
    print(' '.join(map(str, counting_sort(sequen))))
