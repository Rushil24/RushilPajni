import PyPDF2
import os
os.chdir('D:\\Python\\Udemy-AutomateTheBoringStuff\\Excel , Work and PDF Documents\\Reading and Editing PDF')
a = open('Python_Programming_Assignment-ITP_2021.pdf','rb')
reader = PyPDF2.PdfFileReader(a)
b = reader.numPages #this will print the number of pages in Pdf
#page = reader.getPage(0) 
#c = page.extractText() #reads the first page , not correctly but it reads
for pageNum in range(b):
    print(reader.getPage(pageNum).extractText()) #this will read all pages
