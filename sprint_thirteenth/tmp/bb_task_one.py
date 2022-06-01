import random


def partition(competitors, left, right):
    pivot = (competitors[left])
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
    competitors[1] = - int(competitors[1])
    competitors[2] = int(competitors[2])
    return [competitors[1], competitors[2], competitors[0]]


def valid_n_partic():
    pass


def valid_transformation():
    pass


if __name__ == '__main__':
    n_partic = int(input())
    valid_n_partic()
    competitors = [transformation(input().split()) for _ in range(n_partic)]
    quick_sort(competitors, low=0, high=n_partic - 1)
    print(*(list(zip(*competitors))[2]), sep="\n")
