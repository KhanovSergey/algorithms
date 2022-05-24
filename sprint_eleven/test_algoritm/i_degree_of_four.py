def main():
    f = int(input())
    four = []
    count = 0
    i = 0
    end = 10000
    while count < end:
        count = 4**i
        if count < end:
            four.append(count)
            i += 1
    if f in four:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()
