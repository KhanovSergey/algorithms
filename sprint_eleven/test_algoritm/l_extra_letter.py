def main():
    s = input()
    t = input()

    sort_s = sorted(s)
    sort_s.append(None)
    sort_t = sorted(t)

    for i in range(len(sort_t)):
        if sort_s[i] != sort_t[i]:
            print(sort_t[i])
            break


if __name__ == '__main__':
    main()
