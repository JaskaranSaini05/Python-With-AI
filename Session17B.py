# List of months
months_list = ['jan','feb','march',
              'april','may','june',
              'july','aug','sep',
              'oct','nov','dec']

college_attendance = {}.fromkeys(months_list,100)
print('college_attendance')
print(college_attendance)

# How to create a dictionary with list,having keys as elements of list
college_attendance['jan'] -= 5
print('college_attendance')
print(college_attendance)

students ={101,102,103,104,105,106,107,108,109,110}

students_list = {}.fromkeys(students,100)
print('students_list')
print(students_list)