def bubble(sequen, n):
    sequen_ok = sequen
    flag = 0
    for i in range(n - 1):
        flag_cnt = 0
        for j in range(n - 1 - i):
            if sequen[j] > sequen[j + 1]:
                sequen[j], sequen[j + 1] = (
                    sequen[j + 1], sequen[j])
                flag_cnt += 1
        if flag_cnt != 0:
            flag = 1
            print(*sequen)
    if flag != 1:
        print(*sequen_ok)


if __name__ == '__main__':
    n = int(input())
    sequen = [int(num) for num in input().split(' ')]
    bubble(sequen, n)
