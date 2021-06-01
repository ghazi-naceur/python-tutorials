def print_name(name="default"):
    print(f"Name : {name}")


def return_tuple(string):
    print(f'Input : {string}')
    return ("something", "someone")


def repeat(name):
    while name not in ["Isaac", "Netero", "Aizakku"]:
        name = input("What's the name of the hunters association head ?")
    return print("It's Isaac Netero")


def args_function(*args):
    return sum(args) * 0.5


def kwargs_function(**kwargs):
    if 'name' in kwargs:
        print(f"Name : {kwargs['name']}")
    else:
        print("No name mentioned")


def arguments_combination(*args, **kwargs):
    print(f"Name : {args[0]} {kwargs['name']}")


if __name__ == '__main__':
    help([1, 2, 3].insert(1, 4))

    print_name("Netero")
    print_name()

    key, value = return_tuple("today")
    print(key)
    print(value)

    repeat("Someone")

    print(args_function(1, 2, 5))
    print(args_function(1, 2, 5, 56, 100, 1254, 12547, 123698))

    kwargs_function(name="Isaac", age=125)
    kwargs_function(age=125)

    arguments_combination("Isaac", "Takamora", name="Netero", age=125)
