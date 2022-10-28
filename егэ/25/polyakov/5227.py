# dop = 500_000_002
dop = 100
count = 0
k = 1
while count != 5:
    print(k)
    x = dop + k
    p = 2
    cur_del_count = 0
    while x != 1:
        if x % p == 0:
            cur_del_count += 1  # 2
            x = x // p  # 1
        else:
            # найти след простое число
            isPrime = False
            next = p + 1  # 4
            while not isPrime:
                for i in range(2, int(next ** 0.5) + 1):
                    if next % i == 0:
                        next += 1
                        break
                else:
                    p = next  # 3
                    isPrime = True

    if cur_del_count <= 2:
        print("---->", dop + k)
        count += 1
    k += 1
