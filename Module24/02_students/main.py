from student_class import Student

def average_marks_append():
    for student in students:
        average_marks_list.append(student.average_mark)
    average_marks_list.sort()

def student_list_sorting():
    position = 0
    start = 0

    for a_mark in average_marks_list:
        for s_num in range(start, len(students)):
            if a_mark == students[s_num].average_mark:
                students[position], students[s_num] = students[s_num], students[position]
                position += 1
                break
        start += 1


average_marks_list = []
students = [Student('A Z', '1917'), Student('B X', '2021'), Student('K Y', '2020'),
            Student('G H', '2019'), Student('Q W', '2018'), Student('E R', '2017'),
            Student('T Y', '2016'), Student('U I', '2015'), Student('A S', '2014'),
            Student('D F', '2013')]

average_marks_append()
student_list_sorting()

for student in students:
    student.print_info()