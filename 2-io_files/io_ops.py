if __name__ == '__main__':
    my_file = open("../resources/file.txt")
    print(my_file.read())
    print(my_file.read())  # It won't read it again. To read the file again, you need to set the cursor to 0 and re-read
    # your file :
    my_file.seek(0)
    print(my_file.read())

    my_file.seek(0)
    print(my_file.readline())  # The first line

    my_file.seek(0)
    print(my_file.readlines())  # Lines as a list

    my_file.close()
    # We need to close the file, once we finished processing it.
    # There is another way to open a file, and no longer need to worry about closing a file :
    with open("../resources/file.txt") as new_file:
        print("New file :")
        contents = new_file.read()
        print(contents)
        # No need to close the file

    with open("../resources/file.txt", mode='r') as new_file_2:
        print("New file 2:")
        contents = new_file_2.read()
        print(contents)

    with open("../resources/file.txt", mode='w') as new_file_3:
        print("New file 3:")
        # This file won't be readable at this stage, because we chose 'w' : permissions
        # 'w': overwrite the file content
        new_file_3.write("This is a new line .. The old content was overwritten")

    with open("../resources/file2.txt", mode='a') as new_file_4:
        print("New file 4:")
        new_file_4.write("\nThis is a fourth line")

    with open("../resources/file2.txt", mode='a+') as new_file_5:
        print("New file 5:")
        new_file_5.write("\nAdding a fifth line")
        new_file_5.seek(0)
        print(new_file_5.readlines())

    with open("../resources/generated.txt", mode='w') as new_file_6:
        print("New file 6:")
        new_file_6.write("Generating a new file and inserting content in it")

    with open("../resources/generated.txt", mode='r') as new_file_7:
        print(new_file_7.read())