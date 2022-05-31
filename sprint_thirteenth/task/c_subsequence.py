def main(s, t):
    index = 0
    res = False
    for i in s:
        try:
            new_index = t.index(i, index)
            index = new_index + 1
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
    print(main(s, t))
