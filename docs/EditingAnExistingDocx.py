import docx
import os
a = docx.Document('D:\\Python\\Udemy-AutomateTheBoringStuff\\Excel , Work and PDF Documents\\Reading and Editing Word Document\\DocumentsMade\\Used\\demo.docx')
b = a.paragraphs[1] #it will print the location of paragraph
c = b.text #it will print the text in paragraph
d = b.runs #it will print how many times the paragraph will rune ie. one time for italics , bold , etc etc
e = d[0].text #this will print the first run of the paragraph
f = d[0].underline #this will print the type of the word ie. bold,italic,underline
d[0].text = 'italic and underline'
a.save('Made1.docx')
os.getcwd()