import time
import random

GIGABYTE = 1024 * 1024 * 1024
MEGABYTE = 1024 * 1024
KILOBYTE = 1024

list_of_test = ['dict',
                'set',
                'list_append',
                'list_insert',
                ]


def timer(func):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f'\n{func.__name__} took {runtime:.4f} secs\n')
        return result

    return _wrapper


@timer
def random_data_insert_test(datatype, length):
    match datatype:
        case 'dict':
            rand_dict = {}
            for i in range(length):
                rand_dict[i] = i
                print(f'\rstep {datatype}: {i}/{length}', end='')

        case 'list_append':
            rand_list = []
            for i in range(length):
                rand_list.append(i)
                print(f'\rstep {datatype} random insert: {i}/{length}', end='')

        case 'list_insert':
            rand_list = []
            for i in range(length):
                rand_list.insert(random.randint(0, i), i)
                print(f'\rstep {datatype}: {i}/{length}', end='')

        case 'set':
            rand_set = set()
            for i in range(length):
                rand_set.add(i)
                print(f'\rstep {datatype}: {i}/{length}', end='')


if __name__ == '__main__':
    for _ in list_of_test:
        random_data_insert_test(_, MEGABYTE)
