def func1(n):
    return [str(num) for num in range(n)]


def func2(n):
    return list(map(str, range(n)))


if __name__ == '__main__':

    import time

    start_time_func1 = time.time()
    func1(10000000)
    end_time_func1 = time.time()
    print(f"Elapsed time func 1 = {end_time_func1 - start_time_func1}")

    start_time_func2 = time.time()
    func2(10000000)
    end_time_func2 = time.time()
    print(f"Elapsed time func 2 = {end_time_func2 - start_time_func2}")

    import timeit

    statement1 = '''
    func1(100)
    '''

    statement2 = '''
    func2(100)
    '''

    setup1 = '''
def func1(n):
    return [str(num) for num in range(n)]
    '''

    setup2 = '''
def func2(n):
    return list(map(str, range(n)))
    '''

    result1 = timeit.timeit(statement1, setup1, number=100000)
    print(f"Elapsed time func 1 = {result1}")

    result2 = timeit.timeit(statement2, setup2, number=100000)
    print(f"Elapsed time func 2 = {result2}")
