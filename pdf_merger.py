import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write('combined_docs.pdf')

print('files merged into "combined_docs.pdf" file')
