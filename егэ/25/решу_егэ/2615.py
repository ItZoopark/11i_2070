for x in range(525784203, 728943762 + 1):
    cur_count = 0
    max_del = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i == x // i:
                cur_count += 1
            else:
                cur_count += 2

            if x // i > max_del:
                max_del = x // i

        if cur_count > 3:
            break

    if cur_count == 3:
        print(x, max_del)
