student = {
    101:'John',
    102:'Jennie',
    501:'Sia',
    99:'Joe',
    242:'kim',
    453:'Anne',
    242:'Aman'
}

# List of months
months_list = ['jan','feb','march',
              'april','may','june',
              'july','aug','sep',
              'oct','nov','dec']

college_attendance = {}.fromkeys(months_list,100)
print('college_attendance')
print(college_attendance)

keys = list (student.keys())
attendance = {}.fromkeys(keys,100)
attendance_record = {}.fromkeys(keys,attendance)

print()