def factorization(f):
    i = 2
    factoriz = []
    while i * i <= f:
        while f % i == 0:
            factoriz.append(i)
            f = int(f / i)
        i = i + 1
    if f > 1:
        factoriz.append(f)
    return factoriz


def main():
    f = int(input())
    print(" ".join(map(str, factorization(f))))


if __name__ == '__main__':
    main()
