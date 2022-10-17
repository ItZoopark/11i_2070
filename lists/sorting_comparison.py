from random import randint
import timeit
import matplotlib.pyplot as plt

buble_sort_time_list = []
embeded_sort_time = []
count_range = range(100, 1000, 100)
for n in count_range:
    a1 = [randint(0, 100) for _ in range(n)]
    a2 = a1[:]

    start1 = timeit.default_timer()
    a2.sort()
    end1 = timeit.default_timer()
    embeded_sort_time.append(end1-start1)

    start2 = timeit.default_timer()
    for i in range(n - 1):  # i = 0
        count = 0
        for j in range(n - i - 1):  # j=0..n-2
            if a1[j] > a1[j + 1]:
                count += 1
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
        if count == 0:
            break
    end2 = timeit.default_timer()
    buble_sort_time_list.append(end2 - start2)

plt.plot(count_range, buble_sort_time_list, 'g')
plt.plot(count_range, embeded_sort_time, 'r')

