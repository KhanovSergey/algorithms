"""
ID 68738634
Code edits after the first review.
"""

import random
import re
import sys


def partition(competitors, left, right):
    pivot = competitors[left]
    i = left + 1
    j = right - 1
    while True:
        if i <= j and competitors[j] > pivot:
            j -= 1
        elif i <= j and competitors[i] < pivot:
            i += 1
        elif competitors[j] > pivot or competitors[i] < pivot:
            continue
        if i <= j:
            competitors[i], competitors[j] = competitors[j], competitors[i]
        else:
            competitors[left], competitors[j] = competitors[j], competitors[left]
            return j


def quick_sort(array, low, high):
    if low >= high:
        return -1

    left, right = low, high
    pivot = array[random.randint(low, high)]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quick_sort(array, low=low, high=right)
    quick_sort(array, low=left, high=high)


def transformation(competitors):
    valid_competitors(competitors)
    competitors[1] = -int(competitors[1])
    competitors[2] = int(competitors[2])
    return [competitors[1], competitors[2], competitors[0]]


def valid_n_partic(n_partic):
    if not n_partic.isnumeric():
        print(f'Вы ввели {n_partic}, требуется ввести число'
              f' от 1 до 100 000 включительно.')
        sys.exit(1)
    elif 1 > int(n_partic) > 100000:
        print(f'Вы ввели {n_partic}, требуется ввести число'
              f' от 1 до 100 000 включительно.')
        sys.exit(1)


def valid_competitors(competitors):
    pat = re.compile(r"[a-z]+")
    re_full = re.fullmatch(pat, competitors[0])
    if re_full is None or len(competitors[0]) > 20:
        print(f'Необходимо ввести уникальный логин'
              f'(строкой из маленьких латинских букв'
              f' длиной не более 20)')
        sys.exit(1)

    LEFT_SIDE = 0
    RIGHT_SIDE = 1000000000

    for i in range(1, 3):
        if not competitors[i].isnumeric():
            print(f'Вы ввели {competitors[i]}, требуется ввести число'
                  f' от {LEFT_SIDE} до {RIGHT_SIDE} включительно.')
            sys.exit(1)
        elif LEFT_SIDE > int(competitors[i]) > RIGHT_SIDE:
            print(f'Вы ввели {competitors[i]}, требуется ввести число'
                  f' от 1 до 1 000 000 000 включительно.')
            sys.exit(1)


if __name__ == '__main__':
    n_partic = input()
    valid_n_partic(n_partic)
    competitors = [transformation(input().split()) for _ in range(int(n_partic))]
    quick_sort(competitors, low=0, high=int(n_partic) - 1)
    print(*(list(zip(*competitors))[2]), sep="\n")
