import PyPDF2

pdf_file_obj = open('doc2.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
# print(pdf_reader.documentInfo)
print(pdf_reader.getNumPages())

for page in range(pdf_reader.getNumPages()):

    page_obj = pdf_reader.getPage(page)

    text = page_obj.extract_text()

    print(text.strip())
