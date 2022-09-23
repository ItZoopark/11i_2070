n = int(input("n = "))
k = int(input("k = "))
fn = 1
for i in range(2, n+1): # [2..n]
    fn = fn * i
    # print(f"i={i}, f={f}")
fk = 1
for i in range(2, k+1): # [2..n]
    fk = fk * i

fnk = 1
for i in range(2, n-k+1): # [2..n-k]
    fnk = fnk * i

cnk = fn / (fk * fnk)
print(cnk)