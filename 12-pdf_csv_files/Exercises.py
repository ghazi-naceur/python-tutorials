if __name__ == '__main__':
    import csv

    data = open("../resources/12-pdf_csv_files/find_the_link.csv", encoding='utf-8')
    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    link_str = ''
    for row_num, data in enumerate(data_lines):
        link_str += data[row_num]
    print(link_str)

    import PyPDF2

    f = open("../resources/12-pdf_csv_files/Find_the_Phone_Number.pdf", "rb")
    pdf = PyPDF2.PdfFileReader(f)

    import re
    pattern = r'\d{3}.\d{3}.\d{4}'
    all_text = ''
    for n in range(pdf.numPages):
        page = pdf.getPage(n)
        page_text = page.extractText()
        all_text = all_text + ' ' + page_text

    result = re.findall(pattern, all_text)
    print(result)

    for match in re.finditer(pattern, all_text):
        print(match)

    print(all_text[41808:41808 + 12])