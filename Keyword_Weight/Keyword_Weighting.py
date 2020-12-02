import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
from pikepdf import Pdf

filename ='cba_2020_annual_report.pdf'
pdfFileObj = open(filename,'rb')               #open allows you to read the file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   #The pdfReader variable is a readable object that will be parsed
if pdfReader.isEncrypted:
    with Pdf.open(filename,password="333") as pdf:
        pdf.save("new"+filename)
        filename = "new"+filename
        pdfFileObj = open(filename,'rb')               #open allows you to read the file
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   #The pdfReader variable is a readable object that will be parsed
    #pdfReader.decrypt('')
#num_pages = pdfReader.numPages                 #discerning the number of pages will allow us to parse through all the pages
num_pages = 58
print(pdfReader.numPages)

count = 55
text = ""
                                                            
while count < num_pages:                       #The while loop will read each page
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    
#Below if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

if text != "":
    text = text
    
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
    text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')

    # Now we have a text variable which contains all the text derived from our PDF file.




from gensim.summarization import keywords
import warnings
warnings.filterwarnings("ignore")

values = keywords(text=text,split='\n',scores=True)

data = pd.DataFrame(values,columns=['keyword','score'])
data = data.sort_values('score',ascending=False)
data.to_csv('Keywords.csv')
data.head(10)
