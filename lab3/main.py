import time as t
import gen_random
import print_result
import cm_timer
import unique
import field
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Стол', 'price': None}
]
print('Задача 1:')
print(list(field.field(goods, 'title')))
for i in field.field(goods, 'title', 'price'):
    print(i)

print('Задача 2: ')
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
if __name__ == '__main__':
    result = sorted(data, key = abs, reverse = True)
    print(result)
    result_with_lambda = sorted(data, key = lambda i: abs(i), reverse = True)
    print(result_with_lambda)

print('Задача 3: ')
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
u = unique.Unique(data)
print(list(u))

print('Задача 4: ')
print(list(gen_random.gen_random(5, 1, 3)))

print('Задача 5: ')
with cm_timer.cm_timer_1():
    t.sleep(1)


print('Задача 6: ')
if __name__ == '__main__':
    print('!!!!!!!!')
    print_result.test_1()
    print_result.test_2()
    print_result.test_3()
    print_result.test_4()

