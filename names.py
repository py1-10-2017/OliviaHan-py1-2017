


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printName():
    for i in range (0,len(students)):
        print students[i]["first_name"], students[i]["last_name"]

printName()




users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printName2():
    print 'Students'
    students = users["Students"]
    instructors = users["Instructors"]
    for i in range (0,len(students)):
        counter = i+1
        NumberChar = len(students[i]["first_name"]) + len(students[i]["last_name"])
        print counter, "-", students[i]["first_name"], students[i]["last_name"], "-", NumberChar
    print 'instructors'
    for i in range (0,len(instructors)):
        counter = i+1
        NumberChar = len(instructors[i]["first_name"]) + len(instructors[i]["last_name"])
        print counter, "-", instructors[i]["first_name"], instructors[i]["last_name"], "-", NumberChar


printName2()


# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
