import PyPDF2
import sys

pdffile = sys.argv[1]
pdfreader = PyPDF2.PdfFileReader(pdffile)

# Get the Page count
pageCount = pdfreader.numPages
print("Page Count : ", pageCount)

# Get PDF document information
info = pdfreader.getDocumentInfo()
print("Document Info : ", info)
print("Author : ", info.author)
print("Creator : ", info.creator)
print("Producer :", info.producer)
print("Subject : ", info.subject)
print("Title : ", info.title)

# Extract Page 5 from PDF
page5 = pdfreader.pages[5]
print(page5.extractText())

# Merge two PDF files
merger = PyPDF2.PdfFileMerger()
for pdf in ["automateboringstuff.pdf", "automateboringstuff_copy.pdf"]:
    merger.append(pdf)
merger.write("mergedcopy.pdf")
merger.close()


