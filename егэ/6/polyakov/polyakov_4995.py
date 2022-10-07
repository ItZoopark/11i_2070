
for s in range(1000000, 0, -1):
    s1 = s // 5
    n = 8
    while s1 < 156:
        if (s1 + n) % 3 == 0:
            s1 = s1 + 6
        n = n + 11
    if n == 140:
        print(s)
        break
