"""
I defined two functions named ask_grades and calculate_passing_grade. The former asks the user about the grades of 5 students and saves them in a list. 
The latter calculates the passing grade for a given student. Then, I created a dictionary to keep the information of these 5 students.
Lastly, I created a list to store the passing grades that I transferred from the dictionary and sorted its values in descending order. 
"""

# Homework 3
def ask_grades(studentname):
    studentname_grades = []
    grades = ['midterm', 'project', 'final']
    for grade in grades:
        studentname_grades.append(int(float(input('{} please enter your {} grade: '.format(studentname, grade)))))
    return studentname_grades

def calculate_passing_grade(studentname_grades):
    passing_grade = (studentname_grades[0] * 0.3) + (studentname_grades[1] * 0.3) + (studentname_grades[2] * 0.4)
    return passing_grade

# get grades from the user
watney_grades = ask_grades('Watney')
lewis_grades = ask_grades('Lewis')
kapoor_grades = ask_grades('Kapoor')
purnell_grades = ask_grades('Purnell')
martinez_grades = ask_grades('Martinez')


students_info = {
    'Name Surname': ['Mark Watney', 'Melissa Lewis', 'Vincent Kapoor', 'Rich Purnell', 'Rick Martinez'],
    'Midterm Grade': [watney_grades[0], lewis_grades[0], kapoor_grades[0], purnell_grades[0], martinez_grades[0]],
    'Project Grade': [watney_grades[1], lewis_grades[1], kapoor_grades[1], purnell_grades[1], martinez_grades[1]],
    'Final Grade': [watney_grades[2], lewis_grades[2], kapoor_grades[2], purnell_grades[2], martinez_grades[2]],
    'Passing Grade': [calculate_passing_grade(watney_grades), calculate_passing_grade(lewis_grades), calculate_passing_grade(kapoor_grades), 
                      calculate_passing_grade(purnell_grades), calculate_passing_grade(martinez_grades)]
}

# sort passing grades in descending order
passing_grades = students_info['Passing Grade']    # OR students_info.get('Passing Grade')
passing_grades.sort()    # from min to max
passing_grades.reverse() # from max to min
# print(passing_grades)