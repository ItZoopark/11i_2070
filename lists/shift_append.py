from random import randint
rand_list = [randint(0, 100) for _ in range(10)]
print(rand_list)
# сдвиг вправо на один
p = int(input("Введите величину сдвига: "))
s = int(input("Введите направление сдвига: "))

res = []
for i in range(1, len(rand_list)):
    res.append(rand_list[i])
res.append(rand_list[0])

print(res)
