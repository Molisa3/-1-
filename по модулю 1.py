grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
averages = []
for sublist in grades:
    average = sum(sublist) / len(sublist)
    averages.append(average)
print(averages)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_student_list = sorted(students)
student_book = dict(zip(sorted_student_list, averages))
print(student_book)

