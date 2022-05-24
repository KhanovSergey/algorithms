def main():
    n = int(input())
    f = input().split()
    count = 0
    for word in f:
        if len(word) > count:
            res_word = word
            count = len(word)
    print(res_word)
    print(count)


if __name__ == '__main__':
    main()
