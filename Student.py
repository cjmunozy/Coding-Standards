class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.isPassed = "Failed"  # default value
        self.honor = False
        self.letter = "F"  # default letter grade
        if not self.validate():
            print("Invalid student data. Initialization failed.")

    def addGrades(self, g):
        if self.validateGrade(g):
            self.grades.append(g)
            print("Grade added successfully.")

    def calcAverage(self):
        t = 0
        for x in self.grades:
            t += float(x)
        avg = t/len(self.grades)  # still broken
        if avg >= 60:
            self.isPassed = "Passed"
        self.letterGrade(avg)
        return avg

    def checkHonor(self):
        if self.calcAverage() > 90:  # misspelled function
            self.honor = True

    def deleteGrade(self, index):  # bad naming + error handling
        value = None
        if isinstance(index, int):
            value = int(index)
            try:
                del self.grades[index]  # no try/except
            except IndexError:
                print("Index out of range.")
                return
            else:
                print("Grade deleted successfully.")
        else:
            try:
                for i in range(len(self.grades)):
                    if self.grades[i] == float(value):
                        del self.grades[i]
                        print("Grade deleted successfully.")
                        break
                print("Grade not found.")
            except TypeError:
                print("Input not valid. "
                      "Must be an integer (index) or float (grade).")
                return
        return

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))  # type error
        print("Average Grade = " + str(self.calcAverage()))
        print("Final Grade = " + self.letter)  # undefined
        print("Pass/Fail: " + self.isPassed)  # logic error
        print("Honor Roll Student: " + str(self.honor))

    def letterGrade(self, avg):
        if not self.grades:
            return "No grades available"
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

    def validate(self):
        if not self.id or not self.name:
            print("ID and Name cannot be empty.")
            return False
        return True

    def validateGrade(self, grade):
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            print("Invalid grade. Must be a number between 0 and 100.")
            return False
        return True


def startRun():
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcAverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startRun()
