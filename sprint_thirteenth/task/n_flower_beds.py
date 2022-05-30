def main():
    mans.sort()
    results = []
    NUM = 0
    beds_start, beds_end = mans[NUM]
    NUM += 1
    while NUM < n:
        if beds_start <= mans[NUM][0] <= beds_end:
            _, curr_end = mans[NUM]
            NUM += 1
            if curr_end > beds_end:
                beds_end = curr_end
        else:
            results.append([beds_start, beds_end])
            beds_start, beds_end = mans[NUM]
            NUM += 1
    results.append([beds_start, beds_end])

    return results


if __name__ == '__main__':
    n = int(input())
    mans = [None] * n
    for i in range(n):
        start, end = map(int, input().split())
        mans[i] = [start, end]
    for res in main():
        print(*res)
