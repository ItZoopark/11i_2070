from random import randint
n = int(input("Введите кол-во элементов: "))
p = int(input("Введите число частей: "))
rand_list = [randint(0, 100) for _ in range(n)]
print(rand_list)
for i in range(n//2): # 0..n//2-1
    rand_list[i], rand_list[-(i+1)] = rand_list[-(i+1)], rand_list[i]
print(rand_list)
# print(rand_list.reverse())
print(rand_list[::-1])
firstHalf = rand_list[:n//2]
print(firstHalf[::-1] + rand_list[n//2:][::-1])
# rand_list.sort()
print(rand_list)
# x = 5
# y = 2
# x = x + y  = 7
# y = x - y = 5
# x = x - y = 2