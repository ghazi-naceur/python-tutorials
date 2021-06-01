if __name__ == '__main__':
    increment_list = []
    sum_element = 0
    new_list = [1, 2, 3, 4, 5]

    for x in new_list:
        increment_list.append(x + 1)
        sum_element = sum_element + x
    print(increment_list)
    print(sum_element)

    for letter in "Isaac Netero":
        print(letter)

    new_tuple = (1, 2, 3, 4, 5)
    for _ in new_tuple:
        print("loading...")

    another_list = [(1, 2), (3, 4), (5, 6)]
    for item in another_list:
        print(item)

    # Unpacking
    for (a, b) in another_list:
        print(a)
        print(b)

    yet_another_list = [(1, 2, "a"), (3, 4, "b"), (5, 6, "c")]
    for a, b, c in yet_another_list:
        print(a)
        print(b)
        print(c)

    new_dict = {"a": 1, "b": 2, "c": 3 }
    for item in new_dict:
        print(item)  # Iterating by default on keys
    for item in new_dict.items():
        print(item)  # Iterating on keys and values
    for k, v in new_dict.items():  # .keys(), .values()
        print(k)
        print(v)

    # break : breaks out of the current closest enclosing loop
    # continue : goes to the top of the closest enclosing loop
    # pass : does nothing at all

    for k, v in new_dict.items():  # .keys(), .values()
        pass  # Do nothing, no implementation + do not crash

    for letter in "Isaac":
        if letter == "a":
            continue
        print(letter)

    for letter in "Isaac":
        if letter == "a":
            break
        print(letter)
