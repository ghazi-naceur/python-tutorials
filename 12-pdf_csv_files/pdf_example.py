if __name__ == '__main__':
    # pip install PyPDF2
    import PyPDF2

    # Reading PDF
    f = open("../resources/12-pdf_csv_files/Working_Business_Proposal.pdf", 'rb')  # rb : read binary
    pdf_reader = PyPDF2.PdfFileReader(f)
    print(pdf_reader.numPages)

    page1 = pdf_reader.getPage(0)
    page1_text = page1.extractText()
    print(page1_text)

    f.close()

    #  Writing PDF
    f2 = open("../resources/12-pdf_csv_files/Working_Business_Proposal.pdf", 'rb')
    pdf_reader_2 = PyPDF2.PdfFileReader(f2)
    first_page = pdf_reader_2.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    type(first_page)
    pdf_writer.addPage(first_page)
    pdf_output = open("../resources/12-pdf_csv_files/generated.pdf", "wb")  # wb : write binary
    pdf_writer.write(pdf_output)
    f.close()


    # Exercise
    f3 = open("../resources/12-pdf_csv_files/Working_Business_Proposal.pdf", 'rb')
    pdf_pages_content = []
    pdf_reader_3 = PyPDF2.PdfFileReader(f3)
    for num in range(pdf_reader_3.numPages):
        page = pdf_reader_3.getPage(num)
        pdf_pages_content.append(page.extractText())
    f3.close()
    print(pdf_pages_content)
