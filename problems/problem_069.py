# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# There is pseudocode for you to guide you.


# class Student
class Student:
    # method initializer with required state "name"
    def __init__(self, name):
        # self.name = name
        self.name = name
        # self.scores = [] because its an internal state
        self.scores = []

    # method add_score(self, score)
    def add_score(self, score):
        # appends the score value to self.scores
        self.scores.append(score)

    # method get_average(self)
    def get_average(self):
        # if there are no scores in self.scores
        if len(self.scores) == 0:
            # return None
            return None
        # returns the sum of the scores divided by
        # the number of scores
        else:
            total = 0
            for s in self.scores:
                total += s
            return total / len(self.scores)

student = Student("Malik")

print(student.get_average())    # Prints None
student.add_score(80)
print(student.get_average())    # Prints 80
student.add_score(90)
student.add_score(82)
print(student.get_average())    # Prints 84
