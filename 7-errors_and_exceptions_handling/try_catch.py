def add10(number):
    try:
        result = 10 + number
        return result
    except:
        print("Error")


def ask_for_int():
    while True:
        provided = input("Provide an int : ")
        try:
            result = int(provided)
        except:
            print(f"'{provided}' is not a number ")
            continue
        else:
            print("That's a valid integer")
            break
        finally:
            print("end")


if __name__ == '__main__':
    add10(10)
    add10("10")
    add10(10)

    try:
        f= open("../resources/try_catch.txt", mode='r')
        f.write("something")  # write can't be done with read ('r') permission
    except TypeError:
        print("There was a Type Error")
    except OSError:
        print("There was an OS Error")
    except:
        print("There was an Error")
    finally:
        print("terminated")

    ask_for_int()

    try:
        5/0
    except ZeroDivisionError:
        print("Can't divide by 0")
