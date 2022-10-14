from random import randint
n = int(input("Введите кол-во элементов: "))
a = [randint(0, 100) for _ in range(n)]
print(a)

for i in range(n-1):# i = 0
    for j in range(n-i-1): # j=0..n-2
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)