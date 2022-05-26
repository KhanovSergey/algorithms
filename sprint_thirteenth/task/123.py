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

    def req_comb(digits, path, result):
        if digits == '':
            result.append(path)
            return
        for i in symbolls[digits[0]]:
            print(f'symbolls[digits[0]]      {symbolls[digits[0]]}')
            path += i
            #print(f'path one       {path}')
            print(f'digits[1:]  {digits[1:]}')
            req_comb(digits[1:], path, result)
            #print(f'path two       {path}')
            path = path[:-1]

            #print(f'path two       {path}')

    result = []
    req_comb(n, '', result)
    print(result)
    return result


if __name__ == '__main__':
    n = input()
    for x in combinations(n):
        print(x, end=' ')