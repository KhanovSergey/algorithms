def main():
    n = 4
    m = 3
    f = [[1, 2, 3],
         [0, 2, 6],
         [7, 4, 1],
         [2, 7, 0]]
    nx = 0
    mx = 0
# def main():
#     n = int(input())
#     m = int(input())
#     f = []
#     for i in range(n):
#         row = input().split()
#         for i in range(m):
#             row[i] = int(row[i])
#         f.append(row)
#     nx = int(input())
#     mx = int(input())
    a_sort = []
    if nx + 1 != n:
        n0 = nx + 1
        print(f[n0][mx])
        a_sort.append(f[n0][mx])
    if nx - 1 >= 0:
        n1 = nx - 1
        a_sort.append(f[n1][mx])
    if mx + 1 != m:
        m0 = mx + 1
        a_sort.append(f[nx][m0])
    if mx - 1 >= 0:
        m1 = mx - 1
        a_sort.append(f[nx][m1])

    a_sort.sort()
    for k in a_sort:
        print(k, end=' ')


if __name__ == '__main__':
    main()
