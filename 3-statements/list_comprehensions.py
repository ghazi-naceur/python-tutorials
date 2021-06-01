if __name__ == '__main__':

    isaac = "Issac Netero"
    new_list = []

    for letter in isaac:
        new_list.append(letter)
    # The same as :
    another_list = [letter for letter in isaac]

    print(new_list)
    print(another_list)

    num_list_1 = [num for num in range(1, 10)]
    print(num_list_1)

    num_list_2 = [num * 2 for num in range(1, 10)]
    print(num_list_2)

    num_list_3 = [num ** 2 for num in range(1, 10)]
    print(num_list_3)

    num_list_4 = [num for num in range(1, 10) if num % 2 == 0]
    print(num_list_4)

    celcius = [10,12,65,85,64,23]
    fahrenheit = [((9/5)*temp + 32) for temp in celcius]
    print(fahrenheit)

    # Equivalent to :
    fah = []
    for temp in celcius:
        fah.append((9/5)*temp + 32)
    print(fah)

    results = [x if x%2==0 else 'ODD' for x in range(0,10)]
    print(results)

    # nested loop
    res = []
    for x in [1,2,3]:
        for y in [4,5,6]:
           res.append(x * y)
    print(res)
    # Equivalent to :
    result = [x*y for x in [1,2,3] for y in [4,5,6]]
    print(result)