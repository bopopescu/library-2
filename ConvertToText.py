import docxpy
from PyPDF2 import PdfFileReader
#from django.core.files import File
import os


def convertToText(file):

    try:
        if file.endswith('.pdf'):

            PDF = PdfFileReader(open(file, 'rb'), strict=True)
            if PDF.isEncrypted:
                decrypt = PDF.decrypt('')
                if decrypt == 0:
                    raise Exception("Nope")

                elif decrypt == 1 or decrypt == 2:
                    pass

            text = ''
            r = PDF.getPage(1)
            print(r.getContents())
            for page in PDF.pages:
                text = text + page.extractText()
                #print(text)
            return text

        else:

            text = docxpy.process(file)
            return text

    except Exception as e:
        return e


path = '/home/gtohill/Desktop/test_resumes/Varinder_Singh.pdf'
text = convertToText(path)
print(text)