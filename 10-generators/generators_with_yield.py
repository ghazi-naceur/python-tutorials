def create_cubes(n):
    for x in range(n):
        yield x ** 3  # memory efficient


def generate_fibonaci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def simple_generator():
    for x in range(3):
        yield x


if __name__ == '__main__':
    print(create_cubes(10))  # generator object
    print(list(create_cubes(10)))

    for x in create_cubes(10):
        print(x)

    for number in generate_fibonaci(10):
        print(number)

    for x in simple_generator():
        print(x)

    gen = simple_generator()
    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 2
    # print(next(gen))  # cannot happen, because we yielded only 3 values from 0 to 2

    s_iter = iter("Isaac")  # calling an iterator over a string
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))

