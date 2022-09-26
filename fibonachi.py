n = int(input("n= "))

f = 1
s = 1
print(f, s, end=' ')
for i in range(n-2):
    next = f + s
    f = s
    s = next
    print(next)
    # print(s/f)
