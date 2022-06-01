def gen_binary(count, n_one, n_two, prefix):
    print(count, n_one, n_two, prefix)
    if n_one == 0 and n_two == 0:
        print(prefix)
    else:
        if n_one > 0:
            #print(count, n_one, n_two, prefix)
            gen_binary(count + 1, n_one - 1, n_two, prefix + '(')
        if count > 0 and n_two > 0:
            #print(count, n_one, n_two, prefix)
            gen_binary(count - 1, n_one, n_two - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    count = 0
    n_one, n_two = n, n
    gen_binary(count, n_one, n_two, prefix='')