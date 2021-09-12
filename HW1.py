course = {'CS101': ['3004', 'Haynes', '8:00 a.m.'], 
        'CS102' : ['4501', 'Alvarado', '9:00 a.m.'], 
        'CS103' : ['6755', 'Rich', '10:00 a.m.'],
        'NT110' : ['1244', 'Burke', '11:00 a.m.'],
        'CM241' : ['1411', 'Lee', '1:00 p.m.']}


CourseNum = input('Please enter a course number: ')

if CourseNum in course:
    print (course[CourseNum])
else:
    print('Course number not found!')

