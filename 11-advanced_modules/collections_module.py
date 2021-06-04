from collections import Counter
from collections import defaultdict
from collections import namedtuple

if __name__ == '__main__':

    # 1- Counter
    new_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
    print(Counter(new_list))

    another_list = ["a","a","a","a",1,1,2,2,2,2,2,2,3,3,"x","x","x","x",3,3,3]
    print(Counter(another_list))

    print(Counter("Isaac Netero is a Hunters association former head"))

    letters = "somethingaaadddgggjkjkspsklsp"
    counter = Counter(letters)
    print(counter)
    print(counter.most_common())
    print(counter.most_common(2))

    # 2- Default dictionary
    d = {'a': 10}
    print(d['a'])
    # print(d['not known'])  # Error
    default_d = defaultdict(lambda: 0)

    default_d['b'] = 100
    print(default_d['b'])
    print(default_d['not known'])  # returns default value 0

    # 3- Named tuple
    new_tuple = (1,2,3)
    print(new_tuple[0])

    Hunter = namedtuple('Hunter', ['name', 'age', 'specialty'])
    netero = Hunter(name="Netero", age=125, specialty="Enhancer")
    print(type(netero))
    print(netero)

    print(netero.name)
    print(netero[0])

    print(netero.age)
    print(netero[1])

    print(netero.specialty)
    print(netero[2])
