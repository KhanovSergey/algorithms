def main():
    flow1 = input()
    flow2 = input()

    if len(flow1) >= len(flow2):
        n = len(flow1)
        flow2 = flow2.zfill(n)
    else:
        n = len(flow2)
        flow1 = flow1.zfill(n)

    flow1 = list(flow1)
    flow2 = list(flow2)

    for i in range(len(flow1)):
        flow1[i] = int(flow1[i])
    for i in range(len(flow2)):
        flow2[i] = int(flow2[i])

    if len(flow1) >= len(flow2):
        m = len(flow1)
    else:
        m = len(flow1)

    flag = 0
    sum_flow1_flow2 = []

    for i in reversed(range(m)):
        count = flow1[i] + flow2[i] + flag
        if count == 0:
            sum_flow1_flow2.append(0)
        elif count == 1:
            sum_flow1_flow2.append(1)
            flag = 0
        elif count == 2:
            sum_flow1_flow2.append(0)
            flag = 1
        else:
            sum_flow1_flow2.append(1)
            flag = 1
    if flag == 1:
        sum_flow1_flow2.append(1)

    print("".join(map(str, sum_flow1_flow2[::-1])))


if __name__ == '__main__':
    main()
