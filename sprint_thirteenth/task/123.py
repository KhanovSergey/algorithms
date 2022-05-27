def is_comparison(sequen, j):
    tmp1 = sequen[j + 1] + sequen[j]
    tmp2 = sequen[j] + sequen[j + 1]
    if tmp1 > tmp2:
        return True


def num_strength(sequen, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if is_comparison(sequen, j):
                sequen[j + 1], sequen[j] = sequen[j], sequen[j + 1]
    return ''.join(sequen)


if __name__ == '__main__':
    n = int(input())
    sequen = input().split(' ')
    print(num_strength(sequen, n))
