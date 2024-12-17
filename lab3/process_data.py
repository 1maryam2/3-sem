import json
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1

path = "data_light.json"
with open(path, encoding= 'utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(set(i['job-name'].lower() for i in arg))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    sal = gen_random(len(arg), 100000, 200000)
    new = zip(arg, sal)
    return ['{} зарплата {}'.format(job, salary) for job, salary in new]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
