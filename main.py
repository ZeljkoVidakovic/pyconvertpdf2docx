
from pdf2docx import Converter

pdfFile = "filename.pdf"
docxFile = "filename.docx"

cv = Converter(pdfFile)
cv.convert(docxFile)

cv.close()
