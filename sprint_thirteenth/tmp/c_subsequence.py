def main():
    idx = 0
    res = False
    for i in s:
        try:
            new_idx = t.index(i, idx)
            idx = new_idx + 1
            res = True
        except ValueError:
            res = False
            break
    if len(s) == 0:
        res = True
    return res


if __name__ == '__main__':
    s = input()
    t = input()
    print(main())
