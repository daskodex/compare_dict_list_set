import time
import random

GIGABYTE = 1024*1024*1024
MEGABYTE = 1024*1024
KILOBYTE = 1024


def timer(func):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f'\n{func.__name__} took {runtime:.4f} secs')
        return result
    return _wrapper

@timer
def random_dict_insert(length):
    rand_dict = {}
    for i in range(length):
        rand_dict[i] = i
        print(f'\r step dict: {i}/{length}', end='')

    else:
        return True

@timer
def random_list_append(length):
    rand_list = []
    for i in range(length):
        rand_list.append(i)
        print(f'\r step list random insert: {i}/{length}', end='')

    else:
        return True

@timer
def random_list_insert(length):
    rand_list = []
    for i in range(length):
        rand_list.insert(random.randint(0, i), i)
        print(f'\r step list append: {i}/{length}', end='')

    else:
        return True


@timer
def random_set_append(length):
    rand_set = set()
    for i in range(length):
        rand_set.add(i)
        print(f'\r step list set insert: {i}/{length}', end='')

    else:
        return True

if __name__ == '__main__':
    random_dict_insert(MEGABYTE)
    random_set_append(MEGABYTE)
    random_list_append(MEGABYTE)
    random_list_insert(MEGABYTE)

