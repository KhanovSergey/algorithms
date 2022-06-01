import random


def partition(competitors, left, right):
    pivot = (competitors[left])
    print(f'pivot   {pivot}')
    i = left + 1
    print(f'i     {i}')
    j = right - 1
    print(f'j     {j}')
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


# def quick_sort(competitors, left, right):
#     if (right - left) > 1:
#         p = partition(competitors, left, right)
#         print(f'p         {p}')
#         quick_sort(competitors, left, p)
#         quick_sort(competitors, p + 1, right)
#

def quick_sort(array, low, high):
    if low >= high:
        return -1

    left, right = low, high
    pivot = array[random.randint(low, high)]
    print(f'pivot_q_s   {pivot}')
    while left <= right:
        print(f'array[left] w1    {array[left]}')
        while array[left] < pivot:
            print(f'array[left] w2   {array[left]}')
            left += 1
        while array[right] > pivot:
            print(f'array[right] w3   {array[right]}')
            right -= 1
        if left <= right:
            print(f'array[left] i1    {array[left]}')
            print(f'array[right] i1   {array[right]}')
            array[left], array[right] = array[right], array[left]
            print(f'array[left] i1    {array[left]}')
            print(f'array[right] i1   {array[right]}')
            left += 1
            right -= 1

    quick_sort(array, low=low, high=right)
    quick_sort(array, low=left, high=high)

def transformation(competitors):
    competitors[1] = - int(competitors[1])
    competitors[2] = int(competitors[2])
    print([competitors[1], competitors[2], competitors[0]])
    return [competitors[1], competitors[2], competitors[0]]


def valid_n_partic():
    pass

def valid_transformation():
    pass


if __name__ == '__main__':
    # n_partic = int(input())
    n_partic = 5
    valid_n_partic()
    #competitors = [transformation(input().split()) for _ in range(n_partic)]
    competitors = [[-4, 100, 'alla'], [-6, 1000, 'gena'], [-2, 90, 'gosha'], [-2, 90, 'rita'], [-4, 80, 'timofey']]
    print(competitors)
    quick_sort(competitors, low=0, high=n_partic-1)
    #print(f'quick_sort(competitors, LEFT, n_partic) {quick_sort(competitors,  low=0, high=n_partic-1)}')
    print(*(list(zip(*competitors))[2]), sep="\n")

"""
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80

"""