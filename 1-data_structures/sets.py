if __name__ == '__main__':
    new_set = set()
    new_set.add("one")
    new_set.add("one")
    new_set.add("one")
    new_set.add(2)
    new_set.add("three")
    new_set.add("three")
    new_set.add("three")
    print(new_set)

    my_list = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
    print(set(my_list)) # Casting a list as a set