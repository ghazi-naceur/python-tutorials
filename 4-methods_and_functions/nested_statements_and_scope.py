def printer():
     x = 50
     return x

if __name__ == '__main__':

    x = 25
    printer()
    print(x)
    print(printer())

    # Global scope (3rd level scope)
    name = "Global"
    def greet():
        # Enclosing function scope (2nd level scope)
        name = "Enclosing"
        def hello():
            # Local name space scope (1st level scope)
            name = "Local"
            print("Hello "+ name)

        hello()
    greet()

    # Build-in function scope (4th level scope) : function names in this scope shouldn't be overridden : like len, print, sum, max, min ...etc

    x = 50
    def func(x):
        print(f"x : {x}")
        x = 2
        print(f"Updated x : {x}")

    func(20)
    print(x)

    def func2():
        global x  # defining x as a global variable
        print(f"x : {x}")
        x = "2xR"
        print(f"Updated x : {x}")

    func2()
    print(x)