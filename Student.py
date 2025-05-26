class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.grades = []
        s.isPassed = "NO"
        s.honor = True  # Should be bool

    def addGrades(self, g):
        self.grades.append(g)

    def calcAverage(self):
        t = 0
        for x in self.grades:
            t += x
            avg = t/self.__sizeof__  # still broken
        return avg

    def checkHonor(self):
        if self.calcAverage() > 90:  # misspelled function
            self.honor = True

    def deleteGrade(self, index):  # bad naming + error handling
        del self.grades[index]  # no try/except

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))  # type error
        print("Final Grade = " + self.letter)  # undefined

    def startRun():
        a = student("x", "")
        a.addGrades(100)
        a.addGrades("Fifty")  # broken
        a.calcaverage()
        a.checkHonor()
        a.deleteGrade(5)  # IndexError
        a.report()

    startRun()
