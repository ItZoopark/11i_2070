from random import randint

n = int(input("Введите кол-во элементов: "))
a1 = [randint(0, 100) for _ in range(n)]
a2 = a1[:]
# print(f"original: {a1}")

a1.sort()
countAll1 = 0
for i in range(n - 1):  # i = 0
    count = 0
    for j in range(n - i - 1):  # j=0..n-2
        if a1[j] > a1[j + 1]:
            count += 1
            a1[j], a1[j + 1] = a1[j + 1], a1[j]
    countAll1 += count
    if count == 0:
        break
# print(a1)
print(countAll1)

countAll2 = 0
for i in range(n - 1):  # i = 0
    for j in range(n - i - 1):  # j=0..n-2
        countAll2 += 1
        if a2[j] > a2[j + 1]:
            a2[j], a2[j + 1] = a2[j + 1], a2[j]
# print(a2)
print(countAll2)


