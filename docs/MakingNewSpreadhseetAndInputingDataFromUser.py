import openpyxl
import os
print("We Are Making An Excel Of 1 Sheet Having 2 Values In It Of Your Choice")
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
print("What Value Do You Want To Take In First Cell:")
a = input()
print("What Value Do You Want To Take In Second Cell:")
b = input()
sheet['A1'].value = a
sheet['A2'].value = b
wb.save('Example4.xlsx')
print("We Have Saved You Excel File By Name 'Example4.xlsx'")
print("Do You Know Your Current Working Directory?")
print("For Yes Type : 1")
print("For No Type : 2")
c = int(input())
if c == 1:
    print("Good Then Go Ahead With Your Excel")
elif c==2:
    print("Your Current Working Directory Is : \n")
    print(os.getcwd())
    print("This Is The Address Where You Can Find The Excel You Made")
else:
     print("Pls Enter A Valid Input!!!")
     while (c not in [1,2]):
         print("Do You Know Your Current Working Directory?")
         print("For Yes Type : 1")
         print("For No Type : 2")
         c = int(input())
         if c == 1:
            print("Good Then Go Ahead With Your Excel")
         elif c==2:
            print("Your Current Working Directory Is : \n")
            print(os.getcwd())
            print("This Is The Address Where You Can Find The Excel You Made")
         else:
            print("Pls Enter A Valid Input!!!")