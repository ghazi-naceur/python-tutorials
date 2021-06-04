def func():
    return 1


def hello():
    return "Hello !"


if __name__ == '__main__':
    print(func())
    print(func)

    greet = hello()
    print(greet)

    del hello  # delete hello function
    print(greet)  # works

    def hello(name="Isaac"):
        print(f"This is a hello function")
        def greet():
            return '\t A greet function inside the hello function'
        def welcome():
            return '\t A welcome function inside the hello function'

        print(greet())
        print(welcome())

        print("I am going to return a function :")

        if name == "Isaac":
            return greet
        else:
            return welcome


    print("=======================================")

    hello_greet = hello("Isaac")
    print(hello_greet())  # greet function is accessible

    print("=======================================")

    hello_welcome = hello("Netero")
    print(hello_welcome())  # welcome function is accessible

    print("=======================================")

    def parent():
        def child():
            return "embedded"

        return child

    some_parent = parent()
    print(some_parent())  # returning the child function

    print("=======================================")

    def func():
        return "Hi again !"

    def other(some_def_func):  # Pass-in function to another function
        print("Other code runs here")
        print(some_def_func())

    other(func)

    print("=======================================")

    def new_decorator(original_func):
        def wrap_func():
            print("Some extra code, before the original function")
            original_func()
            print("Some extra code, after the original function")

        return wrap_func


    # The following logic can be replaced by '@new_decorator'
    def func_needs_decorator():
        print("to be decorated")
    decorated = new_decorator(func_needs_decorator)
    decorated()

    @new_decorator  # will pass 'func_needs_decorator_2' inside 'new_decorator' function
    def func_needs_decorator_2():
        print("to be decorated")

    func_needs_decorator_2()