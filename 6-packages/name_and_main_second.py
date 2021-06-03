import name_and_main_first
print("Top level in the second file")
name_and_main_first.func()

if __name__ == '__main__':
    print("The second file is being run directly")
else:
    print("The second file has been imported")
