
import pandas as pd 
import numpy as np 
import PyPDF2 
import textract 
import re


#open the file to  read the text

file_name=r'C:\backup\KAVITHA_BACKUP\Personal\DS_Kaggle\pdf_extract\sample_file.pdf'

pdf_obj=open(file_name,'rb')

pdf_reader=PyPDF2.PdfFileReader(pdf_obj)

pdf_num_pages=pdf_reader.numPages

pdf_num_pages

cnt=0
text=''

while cnt<pdf_num_pages :
    pagenum=pdf_reader.getPage(cnt)
    cnt+=1
    text+=pagenum.extractText()
    cnt
    text

#check if the above library returned all words.It's done because PyPDF2 cannot read scanned files

if text != "":
    text = text
 
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
    text = textract.process(file_name, method='pdfminer')

    # Now we have a text variable which contains all the text derived from our PDF file.
text


#find a given word
def find_nxt_word(find):
    find=find.upper()
    words=text.split()
    array_words=[re.sub(r'\W+','',x) for x in words]
    array_words
    
    matches = [array_words[a+1] for a,x in enumerate(array_words) if x.upper()==find]
    return(matches)

# for a,x in enumerate(words):
#     if x=='Name:':
#         #a=a+1
#         words[a+1]

find_nxt_word('address')