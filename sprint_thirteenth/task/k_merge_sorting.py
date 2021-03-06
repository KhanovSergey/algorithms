def merge(arr, lf, mid, rg):
    first = arr[lf: mid]
    second = arr[mid: rg]
    l_first = len(first)
    l_second = len(second)
    f_idx = 0
    s_idx = 0
    result = []
    while True:
        first_elem = first[f_idx]
        second_elem = second[s_idx]
        if first_elem < second_elem:
            result += [first_elem]
            f_idx += 1
        else:
            result += [second_elem]
            s_idx += 1
        if f_idx == l_first:
            ended = 1
            break
        if s_idx == l_second:
            ended = 2
            break
    if ended == 2:
        while f_idx < l_first:
            result += [first[f_idx]]
            f_idx += 1
    else:
        while s_idx < l_second:
            result += [second[s_idx]]
            s_idx += 1
    return result


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf: rg] = merge(arr, lf, mid, rg)
    return arr


if __name__ == '__main__':
    sequen = input().split()
    len_seq = len(sequen)
    for i in range(len_seq):
        sequen[i] = int(sequen[i])

    print(merge_sort(sequen, 0, len_seq))
