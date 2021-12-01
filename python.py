import math

# Class Grader
class Grader():
    # Constructor
    def __init__(self):
        # Properties
        self.name = self
        self.course = self
        self.grade = self
        self.letterGrade = self

        # Calling class methods to run when creating the class
        self.nameQuestion()
        self.outputPrompt()

    # Class methods
    # Student name question method
    def nameQuestion(self):
        self.name = input("What is your name? If the name is more than 1 word use '_' to connect them. ")

        if(self.stringValidation(self.name) == True):
            self.courseQuestion()
        else:
            self.nameQuestion()

    # Course question method
    def courseQuestion(self):
        self.course = input("What is the course name? If the course is more than 1 word use '_' to connect them. ")

        if(self.stringValidation(self.course) == True):
            self.gradeQuestion()
        else:
            self.courseQuestion()

    # Grade question method
    def gradeQuestion(self):
        self.grade = input("What was the grade value? Please enter a value from 0 - 100 ")

        if(self.floatValidation(self.grade) == True):
            self.letterGradeAssigner(self.grade)
        else:
            self.gradeQuestion()

    def outputPrompt(self):
        print(f"{self.name}'s grade in {self.course} was a(n) {self.grade} which is a(n) {self.letterGrade}!")

    # String validation method
    def stringValidation(self, string):
        if(string.isidentifier() == True):
            return True
        else:
            print('Please enter a valid value and/or do not leave blank!')
            return False

    # Integer validation method
    def floatValidation(self, num):
        try:
            num = float(num)

            if(num >= 0 and num <= 100):
                return True
            else:
                print('Please enter a value between 0 - 100')
                return False
        except:
            print('Please enter a valid value and/or do not leave blank!')
            return False

    # Grade assigner method
    def letterGradeAssigner(self, num):
        num = float(num)
        num = math.trunc(num)

        if(num <= 100 and num >= 90):
            self.letterGrade = "'A'"
        elif(num <= 89 and num >= 80):
            self.letterGrade = "'B'"
        elif(num <= 79 and num >= 70):
            self.letterGrade = "'C'"
        elif(num <= 69 and num >= 60):
            self.letterGrade = "'D'"
        else:
            self.letterGrade = "'F'"

# Creating new class grader object
newGrader = Grader()

