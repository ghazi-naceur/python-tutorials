def add(element1, element2):
    return element1 + element2


def multiply(element1, element2):
    return element1 * element2


def get_type(x):
    return type(x)


def get_char(string, position):
    return string[position]


def slice_string(string, start, stop, step):
    return string[start:stop:step]


def get_prefix(string, stop):
    return string[:stop]


def get_suffix(string, start):
    return string[start:]


def get_substring(string, start, stop):
    return string[start:stop]


def get_char_with_step(string, step):
    return string[::step]


def get_length(string):
    return len(string)


def reverse_string(string):
    return string[::-1]


if __name__ == '__main__':
    print(add("1", "3"))
    print(add(1, 3))
    print(add(1.0, 3.0))

    print(multiply("something", 3))
    print(multiply(2, 3))
    print(multiply(2.0, 3.0))

    print(get_type("string value"))
    print(get_type(3))
    print(get_type(2.0))

    print(get_char("Netero", 4))
    print(get_char("Netero", -2))

    print(slice_string("Isaac Netero", 2, 10, 1))
    print(slice_string("Isaac Netero", 0, 10, 1))

    print(get_prefix("Isaac Netero", 10))
    print(get_prefix("Isaac Netero", 10))

    print(get_suffix("Isaac Netero", 10))
    print(get_suffix("Isaac Netero", 10))

    print(get_substring("Isaac Netero", 3, 9))
    print(get_substring("Isaac Netero", 3, 7))

    print(get_char_with_step("Isaac Netero", 2))

    print(get_length("Isaac Netero"))

    print(reverse_string("Isaac Netero"))

    # Uppercase
    print("Isaac netero".upper())

    # Split
    print("Isaac Netero is the former president of the Hunters association".split(" "))

    # Format
    print("Isaac Netero is a {}".format("hunter"))
    print("{} {} {}".format("Isaac", "Netero", "is a hunter"))
    print("{1} {2} {0}".format("is a hunter", "Isaac", "Netero"))
    print("{a} {b} {c}".format(a="Isaac", b="Netero", c="is a hunter"))
    result = 100 / 177
    print("The result was {}".format(result))
    print("The result was {r}".format(r = result))
    print("The result was {r:1.3f}".format(r = result))
    print("The result was {r:1.4f}".format(r = result))
    print("The result was {r:10.4f}".format(r = result))

    # Literal
    name = "Netero"
    age = 125
    print(f"It's Isaac {name}({age})")