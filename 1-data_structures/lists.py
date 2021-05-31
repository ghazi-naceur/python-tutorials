if __name__ == '__main__':

    int_list = [1, 2, 3]
    mixed_list = ["this is a string", 1, 5.0, "Netero", 5, 6]
    print(len(int_list))
    print(len(mixed_list))

    another_list = ["one", "two", "three"]
    print(another_list[0])
    print(another_list[1:])
    yet_another_list = ["four", "five"]
    concatenated = another_list + yet_another_list
    print(concatenated)

    concatenated[0] = "ONE"
    print(concatenated)

    concatenated.append("six")
    print(concatenated)

    concatenated.pop()
    print(concatenated)

    concatenated.pop(2)
    print(concatenated)

    unordered_integers = [5,6,8,2,1,56,9]
    unordered_strings = ["s","f","q","v","a","j"]
    unordered_integers.sort()
    unordered_strings.sort()
    print(unordered_integers)
    print(unordered_strings)

    unordered_integers.reverse()
    unordered_strings.reverse()
    print(unordered_integers)
    print(unordered_strings)