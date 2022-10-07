n = round(int(input("высота= "))/2)

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('*', end='')
    print()
osn = k+1
for i in range(1, n):
    for j in range(i):
        print(' ', end='')
    for k in range(osn-2*i):
        print('*', end='')
    print()