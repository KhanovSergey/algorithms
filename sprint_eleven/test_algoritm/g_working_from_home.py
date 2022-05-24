def main():
    n = int(input())
    m = []
    while n >= 1:
        if n % 2 != 0:
            m.append(1)
            n = n // 2
        else:
            m.append(0)
            n = n // 2

    print("".join(map(str, m[::-1])))


if __name__ == '__main__':
    main()
