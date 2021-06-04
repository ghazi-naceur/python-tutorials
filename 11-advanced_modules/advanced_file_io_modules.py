if __name__ == '__main__':
    f = open("../resources/practice.txt", 'w+')
    f.write("This is a new line")
    f.close()

    import os

    print(os.getcwd())  # current working directly
    print(os.listdir())  # current working directly
    print(os.listdir("../resources"))

    # os.unlink("../resources/dst_folder/file.txt")  # deletes file
    # os.rmdir("../resources/dst_folder/file.txt")  # deletes an empty folder
    for folder, sub_folders, files in os.walk("../resources"):
        print(f"The folder '{folder}' contains the sub-folders : '{sub_folders}' and the following files : '{files}'")

    import shutil

    # shutil.move("../resources/src_folder/file.txt", "../resources/dst_folder")
    shutil.copy("../resources/src_folder/file.txt", "../resources/dst_folder")
    # shutil.rmtree("../resources/dst_folder")  # deletes a folder with its content

    import send2trash

    send2trash.send2trash("../resources/dst_folder/file.txt")

