def func():
    print("This is a function")


print("Top level in the first file")


if __name__ == '__main__':
    print("The first file is being run directly")
else:
    print("The first file has been imported")