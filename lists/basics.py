from random import randint
numbers = [29, 0, -4, 123]
# x = [0]*1000 # инициализаия одинаковыми значениями в нужном количестве
first_element = numbers[0]
print(first_element)
last_index = len(numbers) - 1
lastElement = numbers[last_index]
print(lastElement)
# последний элемент
print(numbers[-1])
# опеределение типа данных
print(type(numbers))
# преобразование диапазона в список
print(list(range(0, 100, 2)))
# list comprehension - списочное выражение
print([x**2 for x in range(100)])
# генерация списка рандомных чисел
rand_list = [randint(0, 100) for _ in range(100)]
print(rand_list)
# срезы
# print(rand_list[2:10])
# print(rand_list[:10])
# print(rand_list[-10:])
# print(rand_list[:])
copy_rand_list = rand_list[:]
copy_rand_list[0] = 1000
print("original: ", rand_list)
print("copy: ", copy_rand_list)
# операции со списками
a = []
for i in range(100):
    x = randint(1, 10)
    if x not in a:
        a.append(x)
print(a)


