class College:
    def __init__(self):
        print("This is non parametrized constructor")
        
    def getCollege(self,clg_name):
        self.clg_name=clg_name
        
    def printCollege(self):
        print("Your college is:", self.clg_name)
        
class Student(College):
    
    def __init__(self,name,rollno):
        print("This is parametrized constructor")
        self.name=name
        self.rollno=rollno

    def printDetails(self):
        print("Student Name:",self.name)
        print("Student Roll Number:",self.rollno)
        
        
#main code
S= Student("lubhani",92)
S.getCollege("igdtuw")
S.printCollege()
S.printDetails()