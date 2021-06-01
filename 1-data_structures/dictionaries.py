if __name__ == '__main__':

    persons = {"name": "Netero", "age": 125}
    print(persons["name"])

    nested = {"k1":1.2, "k2": "something", "k3": ["a",2,"c"], "k4": {"name": "Netero", "age": 125}}

    print(nested["k3"])
    print(nested["k4"])
    print(nested["k4"]["name"])
    nested["k3"][2] = nested["k3"][2].upper()
    print(nested["k3"])

    nested["k5"] = "new value"
    print(nested)

    nested["k1"] = "updated"
    print(nested)

    print(nested.keys())
    print(nested.values())
    print(nested.items())

