h = int(input("h= "))

f = 0
s = 1
t = 1
for i in range(h):
    n = f + s + t
    f = s
    s = t
    t = n
    print(n, end=' ')