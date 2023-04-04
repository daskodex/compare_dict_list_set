import time
import random

GIGABYTE = 1024 * 1024 * 1024
MEGABYTE = 1024 * 1024
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
def ranadom_data_insert_test(datatype, length):
    match datatype:
        case 'dict':
            rand_dict = {}
            for i in range(length):
                rand_dict[i] = i
                print(f'\r step dict: {i}/{length}', end='')
        case 'listappend':
            rand_list = []
            for i in range(length):
                rand_list.append(i)
                print(f'\r step list random insert: {i}/{length}', end='')
        case 'listinsert':
            rand_list = []
            for i in range(length):
                rand_list.insert(random.randint(0, i), i)
                print(f'\r step list append: {i}/{length}', end='')
        case 'set':
            rand_set = set()
            for i in range(length):
                rand_set.add(i)
                print(f'\r step list set insert: {i}/{length}', end='')


if __name__ == '__main__':
    ranadom_data_insert_test('dict', MEGABYTE)
    ranadom_data_insert_test('set', MEGABYTE)
    ranadom_data_insert_test('listappend', MEGABYTE)
    ranadom_data_insert_test('listinsert', MEGABYTE)
