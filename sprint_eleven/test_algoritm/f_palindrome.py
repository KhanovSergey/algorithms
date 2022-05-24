import string


def main():
    f = input().lower()
    f = f.replace(' ', '')
    for punct in string.punctuation:
        if punct in f:
            f = f.replace(punct, '')
    count = 0
    flag = 1
    while count < len(f) // 2:
        if f[count] != f[len(f) - count - 1]:
            flag = 0
            break
        count += 1
    if flag == 0:
        print('False')
    else:
        print('True')


if __name__ == '__main__':
    main()
