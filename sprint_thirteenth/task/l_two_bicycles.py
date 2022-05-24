def binarySearch(sequen, s, left, right):
    if right <= left and left != 0:
        return -1

    mid = (left + right) // 2
    if sequen[mid] >= s and sequen[mid - 1] < s or mid == 0:
        return mid + 1
    elif s <= sequen[mid]:
        return binarySearch(sequen, s, left, mid)
    else:
        return binarySearch(sequen, s, mid + 1, right)
    return sequen[mid]


if __name__ == '__main__':
    n = int(input())
    sequen = [int(num) for num in input().split(' ')]
    s = int(input())
    print(binarySearch(sequen, s, left=0, right=len(sequen)), end=' ')
    print(binarySearch(sequen, s * 2, left=0, right=len(sequen)), end=' ')
