if __name__ == '__main__':

    f1 = open("../resources/file_one.txt", 'w+')
    f1.write("This is a file 1")
    f1.close()

    f2 = open("../resources/file_two.txt", 'w+')
    f2.write("This is a file 2")
    f2.close()

    import zipfile

    compressed_file = zipfile.ZipFile("../resources/compressed_file.zip", 'w')
    compressed_file.write('../resources/file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
    compressed_file.write('../resources/file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
    compressed_file.close()

    zip_extracted = zipfile.ZipFile("../resources/compressed_file.zip", 'r')
    # zip_extracted.extract()  # extract 1 specific file
    zip_extracted.extractall("../resources/extracted_content")
    zip_extracted.close()

    import shutil

    dir_to_zip = "../resources/extracted_content"
    output_file_name = "../resources/zipped_again"
    shutil.make_archive(output_file_name, 'zip', dir_to_zip)

    shutil.unpack_archive("../resources/zipped_again.zip", "../resources/unzipped_again", 'zip')