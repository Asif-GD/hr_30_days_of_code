class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   first_name - A string denoting the Person's first name.
    #   last_name - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id_number, scores):
        self.scores = scores
        super().__init__(first_name, last_name, id_number)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate_grade(self):
        average = sum(self.scores) / len(self.scores)
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input())  # not needed for Python
student_scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, student_scores)
s.print_person()
print("Grade:", s.calculate_grade())
