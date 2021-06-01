if __name__ == '__main__':
    tuple = (1,2,3, "four", 5.0, "four", "four")
    list = [1,2,3]
    print(tuple)
    print(list)
    print(len(tuple))
    print(tuple[0])
    print(tuple[-2])
    print(tuple.count("four"))
    print(tuple.index(5.0))

    # tuple[0] = "kfj" # Mutability is not allowed for a tuple