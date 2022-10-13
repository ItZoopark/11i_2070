from random import randint
rand_list = [randint(0, 100) for _ in range(10)]
print(rand_list)
# сдвиг вправо на один
p = int(input("Введите величину сдвига: "))
s = int(input("Введите направление сдвига: "))*(-1)

print(rand_list[s*p:] + rand_list[0:s*p])