def square(num):
    return num ** 2


def splicer(string):
    if len(string) % 2 == 0:
        return 'even'
    else:
        return string[0]


def check_even(num):
    return num % 2 == 0


if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5]

    # map
    for item in map(square, nums):
        print(item)

    num_list = list(map(square, nums))
    print(num_list)

    names = ["Isaac", "Netero", "Takamora", "Shisui", "Itachi"]
    print(list(map(splicer, names)))

    # filter
    for item in filter(check_even, nums):
        print(item)

    print(list(filter(check_even, nums)))

    # lambda
    lambda_square = lambda num: num ** 2

    print(lambda_square(5))

    print(list(map(lambda num: num ** 2, nums)))

    print(list(filter(lambda num: num % 2 == 0, nums)))

    print(list(map(lambda string: string[0], names)))

    print(list(map(lambda string: string[::-1], names)))

    print(list(map(lambda string: string.lower().capitalize(), names)))
