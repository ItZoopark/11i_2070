# Среди целых чисел, принадлежащих числовому отрезку [4099; 26985],
# найдите числа, имеющие ровно один натуральный делитель, не считая единицы и самого числа.
# В ответе запишите два числа: сначала количество найденных чисел, а затем сумму цифр этих чисел.

count = 0
sum_digits = 0
for x in range(4099, 26985 + 1):
    cur_count = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i == x // i:
                cur_count += 1
            else:
                cur_count += 2
            if cur_count > 1:
                break

    if cur_count == 1:
        count += 1
        xc = x
        while xc != 0:
            sum_digits += xc % 10
            xc = xc // 10
print(count, sum_digits)
