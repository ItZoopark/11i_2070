# dop = 500_000_000
dop = 100
x = dop ** 0.5
p = 2
primes = []
while p < x:
    p += 1
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            break
    else:
        primes.append(p)

k = 1
x = dop + k
count_del = 0
count = 0
while count != 5:
    xc = x
    i = 0
    while xc != 1:
        while xc % primes[i] == 0:
            xc = xc // primes[i]
            count_del += 1
            if count_del > 2:
                break
        if i == len(primes)-1:
            break
        i += 1
    if count_del <= 2:
        print(x - dop)
        count += 1
    x += 1
