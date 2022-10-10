a = int(input("a= "))
b = int(input("b= "))
n = int(input("n= "))
print("формула= ", (a+b)**n)
s = 0
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
    s += cnk * a**(n - k) * b**k

print("бином ньютона= ", s)