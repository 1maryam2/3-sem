
def print_result(f):
    def wrapper(*args, **kwargs):
        func = f(*args, **kwargs)
        h = f.__name__
        print(h)
        if isinstance(func, dict):
            for key, item in func.items():
                print(f'{key} = {item}')
        elif isinstance(func, list):
            for i in func:
                print(i)
        else:
            print(func)
        return func
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


