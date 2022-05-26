def num_strength(sequen, n): # ключ сравнения
    sequen_ok = sequen


    for i in range(n - 1):

        for j in range(n - 1 - i):
            #if sequen[i][j] < sequen[i][j + 1]:
            print(f'sequen[i][j]     {sequen[i][j]}')
            print(f'sequen[i+1][j]      {sequen[i+1][j]}')
                # sequen[j], sequen[j + 1] = (
                #     sequen[j + 1], sequen[j])

    #print(*sequen_ok)


if __name__ == '__main__':
    #n = int(input())
    n = 5
    #sequen = [int(num) for num in input().split(' ')]
    sequen = input().split(' ')
    # print(sequen)
    # print(sequen[0][1]) # 2
    # print(len(sequen[0])) # 2
    num_strength(sequen, n)

  # 12 8 9 10 11
  # for i in symbolls[n[0]]:
  #           part += i
  #           req_comb(n[1:], part, result)
  #           part = part[:-1]

