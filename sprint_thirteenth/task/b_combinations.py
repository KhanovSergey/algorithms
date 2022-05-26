def combinations(n):
    symbolls = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }

    def req_comb(n, part, result):
        if n == '':
            result.append(part)
            return
        for i in symbolls[n[0]]:
            part += i
            req_comb(n[1:], part, result)
            part = part[:-1]

    result = []
    req_comb(n, '', result)
    return result


if __name__ == '__main__':
    n = input()
    for i in combinations(n):
        print(i, end=' ')
