from random import randint
rand_list = [randint(0, 100) for _ in range(10)]
print(rand_list)
# сдвиг вправо на один
p = int(input("Введите величину сдвига: "))
s = int(input("Введите направление сдвига: "))
size = len(rand_list)
if s == 1:
    rand_list_1 = rand_list[:]
    for _ in range(p):
        last = rand_list_1[-1]
        for i in range(size-1, 0, -1): #size-1...1
            rand_list_1[i] = rand_list_1[i-1]
        rand_list_1[0] = last
    print("сдвиг вправо", rand_list_1)
elif s == -1:
    rand_list_2 = rand_list[:]
    for _ in range(p):
        first = rand_list_2[0]
        for i in range(size-1): #0...size-2
            rand_list_2[i] = rand_list_2[i+1]
        rand_list_2[-1] = first
    print("сдвиг влево", rand_list_2)
