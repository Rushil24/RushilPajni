class NewDiplomaProgram():
    print("To Know The Result Of Python Programming Course Type: 1")
    print("To Know The Result Of Data Mining and Machine Learning Course Type: 2")
    print("To Know The Result Of Visual Analytics Course Type: 3")
    print("To Know The Result Of Text Analytics Course Type: 4")
    print("To Know Whether You Got A Diploma Certificate Dith Distinction Or Not Type: 5")
    pass10 = 0
    def __init__(self):
        self.pass1 = 0
        self.pass2 = 0
        self.pass3 = 0
        self.pass4 = 0 
class PythonProgrammingCourse(NewDiplomaProgram):
    def __init__(self):
        super().__init__()
    def Assignment1(self):
        print("Python Programming Course:")
        print("What Was Your Result Of Assignment 1 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        a = int(input())
        if a==1:
            print("Assignment 1 : Pass\n")
            self.pass1 += 1
            NewDiplomaProgram.pass10 +=1
        elif a==2:
            print("Assignment 1 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(a not in [1,2] ):
                        print("What Was Your Result Of Assignment 1 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        a = int(input())
                        if a==1:
                            print("Assignment 5 : Pass\n")
                            self.pass1 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif a==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment2(self):
        print("What Was Your Result Of Assignment 2 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        b = int(input())
        if b==1:
            print("Assignment 2 : Pass\n")
            self.pass1 += 1
            NewDiplomaProgram.pass10 +=1
        elif b==2:
            print("Assignment 2 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(b not in [1,2] ):
                        print("What Was Your Result Of Assignment 2 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        b = int(input())
                        if b==1:
                            print("Assignment 5 : Pass\n")
                            self.pass1 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif b==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment3(self):
        print("What Was Your Result Of Assignment 3 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        c = int(input())
        if c==1:
            print("Assignment 3 : Pass\n")
            self.pass1 += 1
            NewDiplomaProgram.pass10 +=1
        elif c==2:
            print("Assignment 3 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(c not in [1,2] ):
                        print("What Was Your Result Of Assignment 3 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        c = int(input())
                        if c==1:
                            print("Assignment 5 : Pass\n")
                            self.pass1 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif c==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment4(self):
        print("What Was Your Result Of Assignment 4 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        d = int(input())
        if d==1:
            print("Assignment 4 : Pass\n")
            self.pass1 += 1
            NewDiplomaProgram.pass10 +=1
        elif d==2:
            print("Assignment 4 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(d not in [1,2] ):
                        print("What Was Your Result Of Assignment 4 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        d = int(input())
                        if d==1:
                            print("Assignment 5 : Pass\n")
                            self.pass1 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif d==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment5(self):
        print("What Was Your Result Of Assignment 5 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        e = int(input())
        if e==1:
            print("Assignment 5 : Pass\n")
            self.pass1 += 1
            NewDiplomaProgram.pass10 +=1
        elif e==2:
            print("Assignment 5 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
        if self.pass1 >=3:
            print("Congratulations You Passed This Program\n")
        else:
            print("You Failed This Program!\n")
            while(e not in [1,2] ):
                        print("What Was Your Result Of Assignment 5 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        e = int(input())
                        if e==1:
                            print("Assignment 5 : Pass\n")
                            self.pass1 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif e==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
#    def __Point1__(self):
#        self.a1 = print(self.pass1)
class DataMiningAndMachineLearningCourse(NewDiplomaProgram):
    def __init__(self):
        super().__init__()
    def Assignment1(self):
        print("Data Mining and Machine Learning Course:")
        print("What Was Your Result Of Assignment 1 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        a = int(input())
        if a==1:
            print("Assignment 1 : Pass\n")
            self.pass2 += 1
            NewDiplomaProgram.pass10 +=1
        elif a==2:
            print("Assignment 1 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(a not in [1,2] ):
                        print("What Was Your Result Of Assignment 1 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        a = int(input())
                        if a==1:
                            print("Assignment 5 : Pass\n")
                            self.pass2 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif a==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment2(self):
        print("What Was Your Result Of Assignment 2 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        b = int(input())
        if b==1:
            print("Assignment 2 : Pass\n")
            self.pass2 += 1
            NewDiplomaProgram.pass10 +=1
        elif b==2:
            print("Assignment 2 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(b not in [1,2] ):
                        print("What Was Your Result Of Assignment 2 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        b = int(input())
                        if b==1:
                            print("Assignment 5 : Pass\n")
                            self.pass2 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif b==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment3(self):
        print("What Was Your Result Of Assignment 3 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        c = int(input())
        if c==1:
            print("Assignment 3 : Pass\n")
            self.pass2 += 1
            NewDiplomaProgram.pass10 +=1
        elif c==2:
            print("Assignment 3 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(c not in [1,2] ):
                        print("What Was Your Result Of Assignment 3 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        c = int(input())
                        if c==1:
                            print("Assignment 5 : Pass\n")
                            self.pass2 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif c==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment4(self):
        print("What Was Your Result Of Assignment 4 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        d = int(input())
        if d==1:
            print("Assignment 4 : Pass\n")
            self.pass2 += 1
            NewDiplomaProgram.pass10 +=1
        elif d==2:
            print("Assignment 4 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(d not in [1,2] ):
                        print("What Was Your Result Of Assignment 4 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        d = int(input())
                        if d==1:
                            print("Assignment 5 : Pass\n")
                            self.pass2 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif d==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment5(self):
        print("What Was Your Result Of Assignment 5 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        e = int(input())
        if e==1:
            print("Assignment 5 : Pass\n")
            self.pass2 += 1
            NewDiplomaProgram.pass10 +=1
        elif e==2:
            print("Assignment 5 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(e not in [1,2] ):
                        print("What Was Your Result Of Assignment 5 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        e = int(input())
                        if e==1:
                            print("Assignment 5 : Pass\n")
                            self.pass2 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif e==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
        if self.pass2 >=3:
            print("Congratulations You Passed This Program\n")
        else:
            print("You Failed This Program!\n")
#   def __Point2__(self):
#        self.b = print(self.pass2) 
class VisualAnalyticsCourse(NewDiplomaProgram):
    def __init__(self):
        super().__init__()
    def Assignment1(self):
        print("Visual Analytics Course:")
        print("What Was Your Result Of Assignment 1 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        a = int(input())
        if a==1:
            print("Assignment 1 : Pass\n")
            self.pass3 += 1
            NewDiplomaProgram.pass10 +=1
        elif a==2:
            print("Assignment 1 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(a not in [1,2] ):
                        print("What Was Your Result Of Assignment 1 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        a = int(input())
                        if a==1:
                            print("Assignment 5 : Pass\n")
                            self.pass3 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif a==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment2(self):
        print("What Was Your Result Of Assignment 2 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        b = int(input())
        if b==1:
            print("Assignment 2 : Pass\n")
            self.pass3 += 1
            NewDiplomaProgram.pass10 +=1
        elif b==2:
            print("Assignment 2 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(b not in [1,2] ):
                        print("What Was Your Result Of Assignment 2 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        b = int(input())
                        if b==1:
                            print("Assignment 5 : Pass\n")
                            self.pass3 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif b==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment3(self):
        print("What Was Your Result Of Assignment 3 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        c = int(input())
        if c==1:
            print("Assignment 3 : Pass\n")
            self.pass3 += 1
            NewDiplomaProgram.pass10 +=1
        elif c==2:
            print("Assignment 3 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(c not in [1,2] ):
                        print("What Was Your Result Of Assignment 3 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        c = int(input())
                        if c==1:
                            print("Assignment 5 : Pass\n")
                            self.pass3 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif c==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment4(self):
        print("What Was Your Result Of Assignment 4 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        d = int(input())
        if d==1:
            print("Assignment 4 : Pass\n")
            self.pass3 += 1
            NewDiplomaProgram.pass10 +=1
        elif d==2:
            print("Assignment 4 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(d not in [1,2] ):
                        print("What Was Your Result Of Assignment 4 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        d = int(input())
                        if d==1:
                            print("Assignment 5 : Pass\n")
                            self.pass3 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif d==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment5(self):
        print("What Was Your Result Of Assignment 5 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        e = int(input())
        if e==1:
            print("Assignment 5 : Pass\n")
            self.pass3 += 1
            NewDiplomaProgram.pass10 +=1
        elif e==2:
            print("Assignment 5 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(e not in [1,2] ):
                        print("What Was Your Result Of Assignment 5 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        e = int(input())
                        if e==1:
                            print("Assignment 5 : Pass\n")
                            self.pass3 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif e==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
        if self.pass3 >=3:
            print("Congratulations You Passed This Program\n")
        else:
            print("You Failed This Program!\n")
#    def __Point3__(self):
#        self.c = print(self.pass3)
class TextAnalyticsCourse(NewDiplomaProgram):
    def __init__(self):
        super().__init__()
    def Assignment1(self):
        print("Text Analytics Course:")
        print("What Was Your Result Of Assignment 1 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        a = int(input())
        if a==1:
            print("Assignment 1 : Pass\n")
            self.pass4 += 1
            NewDiplomaProgram.pass10 +=1
        elif a==2:
            print("Assignment 1 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(a not in [1,2] ):
                        print("What Was Your Result Of Assignment 1 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        a = int(input())
                        if a==1:
                            print("Assignment 5 : Pass\n")
                            self.pass4 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif a==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment2(self):
        print("What Was Your Result Of Assignment 2 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        b = int(input())
        if b==1:
            print("Assignment 2 : Pass\n")
            self.pass4 += 1
            NewDiplomaProgram.pass10 +=1
        elif b==2:
            print("Assignment 2 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(b not in [1,2] ):
                        print("What Was Your Result Of Assignment 2 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        b = int(input())
                        if b==1:
                            print("Assignment 5 : Pass\n")
                            self.pass4 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif b==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment3(self):
        print("What Was Your Result Of Assignment 3 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        c = int(input())
        if c==1:
            print("Assignment 3 : Pass\n")
            self.pass4 += 1
            NewDiplomaProgram.pass10 +=1
        elif c==2:
            print("Assignment 3 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(c not in [1,2] ):
                        print("What Was Your Result Of Assignment 3 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        c = int(input())
                        if c==1:
                            print("Assignment 5 : Pass\n")
                            self.pass4 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif c==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment4(self):
        print("What Was Your Result Of Assignment 4 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        d = int(input())
        if d==1:
            print("Assignment 4 : Pass\n")
            self.pass4 += 1
            NewDiplomaProgram.pass10 +=1
        elif d==2:
            print("Assignment 4 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(d not in [1,2] ):
                        print("What Was Your Result Of Assignment 4 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        d = int(input())
                        if d==1:
                            print("Assignment 5 : Pass\n")
                            self.pass4 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif d==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
    def Assignment5(self):
        print("What Was Your Result Of Assignment 5 ?")
        print("If You Passed Type : 1")
        print("If You Failed Type : 2")
        print("Enter : ")
        e = int(input())
        if e==1:
            print("Assignment 5 : Pass\n")
            self.pass4 += 1
            NewDiplomaProgram.pass10 +=1
        elif e==2:
            print("Assignment 5 : Fail\n")
        else:
            print("Please Enter A Valid Input !!\n")
            while(e not in [1,2] ):
                        print("What Was Your Result Of Assignment 5 ?")
                        print("If You Passed Type : 1")
                        print("If You Failed Type : 2")
                        print("Enter : ")
                        e = int(input())
                        if e==1:
                            print("Assignment 5 : Pass\n")
                            self.pass4 += 1
                            NewDiplomaProgram.pass10 +=1
                        elif e==2:
                            print("Assignment 5 : Fail\n")
                        else:
                            print("Please Enter A Valid Input !!\n")
        if self.pass4 >=3:
            print("Congratulations You Passed This Program\n")
        else:
            print("You Failed This Program!\n")
#    def __Point4__(self):
#        self.d = print(self.pass4)

#class Result(NewDiplomaProgram()):
#    def situation(self) :
#        if NewDiplomaProgram.pass10 >=17:
#            print("Congratulations!! You Got A Diploma Certificate With Distinction")
#        else:
#            print("Sorry!! You Have Not Got Enough Points For A Diploma Certificate With Distinction")

A = int(input())
if A==1:
    a = PythonProgrammingCourse()
    a.Assignment1()
    a.Assignment2()
    a.Assignment3()
    a.Assignment4()
    a.Assignment5()
elif A==2:
    b = DataMiningAndMachineLearningCourse()
    b.Assignment1()
    b.Assignment2()
    b.Assignment3()
    b.Assignment4()
    b.Assignment5()
elif A==3:
    c = VisualAnalyticsCourse()
    c.Assignment1()
    c.Assignment2()
    c.Assignment3()
    c.Assignment4()
    c.Assignment5()
elif A==4:
    d = TextAnalyticsCourse()
    d.Assignment1()
    d.Assignment2()
    d.Assignment3()
    d.Assignment4()
    d.Assignment5()
elif A==5:
    a = PythonProgrammingCourse()
    a.Assignment1()
    a.Assignment2()
    a.Assignment3()
    a.Assignment4()
    a.Assignment5()

    b = DataMiningAndMachineLearningCourse()
    b.Assignment1()
    b.Assignment2()
    b.Assignment3()
    b.Assignment4()
    b.Assignment5()

    c = VisualAnalyticsCourse()
    c.Assignment1()
    c.Assignment2()
    c.Assignment3()
    c.Assignment4()
    c.Assignment5()

    d = TextAnalyticsCourse()
    d.Assignment1()
    d.Assignment2()
    d.Assignment3()
    d.Assignment4()
    d.Assignment5()
    
#    e = Result()
#    e.situation()
else:
    raise AssertionError('Pls Type A Valid Number')

if NewDiplomaProgram.pass10 >=17:
    print("Congratulations!! You Got A Diploma Certificate With Distinction")
else:
    print("Sorry!! You Have Not Got Enough Points For A Diploma Certificate With Distinction")
    