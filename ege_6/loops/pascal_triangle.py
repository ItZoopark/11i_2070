h = int(input("h= "))
for n in range(h+1):
    for k in range(n+1):
        fn = 1
        for i in range(2, n + 1):
            fn = fn * i

        fk = 1
        for i in range(2, k + 1):
            fk = fk * i

        fnk = 1
        for i in range(2, n - k + 1):
            fnk = fnk * i

        cnk = fn // (fk * fnk)
        print(cnk, end=' ')
    print()