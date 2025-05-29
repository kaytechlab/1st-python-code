class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

student1 = Student("kay", [85, 90, 78, 92])
print("Student Name:", student1.name)
print("Average Score:", student1.average())
