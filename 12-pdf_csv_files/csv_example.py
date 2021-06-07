if __name__ == '__main__':

    import csv

    data = open("../resources/12-pdf_csv_files/example.csv", encoding='utf-8')  # we have "@" characters in the
    # "exemple.csv" file, so we should use "encoding='utf-8'"
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    print(data_lines)

    for line in data_lines:
        print(line)

    print(data_lines[10])
    print(data_lines[10][3])

    for line in data_lines[1:15]:
        print(line[3])

    full_names = []
    for line in data_lines:
        full_names.append(line[1] + ' ' + line[2])
    print(full_names)

    file_to_output = open('../resources/12-pdf_csv_files/to_save_file.csv', mode='w', newline='')
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])  # list of list
    file_to_output.close()

    f = open('../resources/12-pdf_csv_files/to_save_file.csv', mode='a', newline='')
    csv_writer_2 = csv.writer(f)
    csv_writer_2.writerow([1,2,3])  # list
    f.close()
