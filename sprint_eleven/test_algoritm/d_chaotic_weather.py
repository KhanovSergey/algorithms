# n = 7
# f = [-1, -10, -8, 0, 2, 0, 5]

def main():
    n = int(input())
    f = input().split()
    for i in range(n):
        f[i] = int(f[i])

    count = 0
    f.insert(0, -274)
    f.append(-274)
    i = 1
    while i < n + 1:
        if (f[i - 1] < f[i] > f[i + 1]):
            count += 1
        i += 1
    print(count)


if __name__ == '__main__':
    main()
