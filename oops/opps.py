"""Create student class that takes name & marks of 3 subjects as arguments in constructor. 
Then create a method to print the average """

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)  # Simplified summation of marks
        avg = total / len(self.marks)  # Calculate average based on the number of marks
        print(f"Hi {self.name}, your average score is: {avg}")



# Create a Student object
s1 = Student("Ayush", [99, 98, 97])

# Call the get_avg method to print the average
s1.get_avg()