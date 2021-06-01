if __name__ == '__main__':
    # range : a generator that generates data instead of saving it in the memory
    print("Testing range :")
    for num in range(5):
        print(num)

    print("Testing range with a defined starting point :")
    for num in range(2, 5):
        print(num)

    print("Testing range with step with a step :")
    for num in range(2, 10, 2):
        print(num)

    new_list = list(range(2, 10, 2))
    print(new_list)

    # enumerate : generating numerated tuples
    for item in enumerate("Isaac Netero"):
        print(item)

    # zip : zips 2 lists
    listA = [1,2,3]
    listB = ["a","b","c"]
    for item in zip(listA, listB):
        print(item)

    listC = ["something","something","something"]
    listD = list(zip(listA, listB, listC))
    print(listD)

    # in
    print('x' in [1,2,3])
    print("k" in {"k":"v"})
    print("k" in {"k":"v"}.keys())
    print("k" in {"k":"v"}.values())

    # min and max
    print(min(new_list))
    print(max(new_list))

    # random
    from random import shuffle
    another_list = [1,2,3,4,5,6,7,8,9]
    shuffle(another_list)
    print(another_list)

    from random import randint
    print(randint(1, 20))

    provided = input("Enter a number : ")  # input always accept things as a string, so you may want to cast the
    # provided input :
    print(f"provided : {int(provided)}")
