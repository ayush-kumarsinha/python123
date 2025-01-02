class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome student", self.name)
        
    def get_marks(self):
        return self.marks

s1 = Student("ayush", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.get_marks())

