import PyPDF2

pdfFileObj = open('automateboringstuff.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Check PDF is password protected
if pdfReader.isEncrypted:
    print("PDF is password protected. Please provide the password to open")
    pdfReader.decrypt('password')
else:
    print("PDF is not password protected")

# Get number of pages
pageCount = pdfReader.numPages
print("Automate Boring Stuff Page Count : ", pageCount)

# Get 0th Page
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
