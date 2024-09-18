# Eva Black
# TummyAKE
# SoftDev
# Title
# description

# 2024-09-17
# Time: start 10:33-10:59

import random

def makeRoster (filename):
    data = open(filename).read()
    
    tuples = data.rsplit("@@@")[:-1]
    names = []
    information = []
    
    for i in range(len(tuples)):
        tuples[i] = tuples[i].rsplit("$$$")
        names.append(tuples[i][1])
        information.append([tuples[i][0], tuples[i][2]])
        
    roster = {}
    
    for i in range(len(names)):
        roster.update({names[i]: information[i]})
        
    return roster
     

def selectRandom(krewes):
    x = random.randrange(len(krewes))
    student_names = list(krewes.keys())
    student_name = student_names[x]
    student_info = krewes[student_name]
    period = student_info[0]
    ducky = student_info[1]

    '''
    x = random.randrange(0, len(krewes))
    pd = list(krewes.keys())[x]
    students = krewes[pd]
    x = random.randrange(0, len(students))
    student = students[x]
    return student
    '''

    return "Period: " + period + ", Name: " + student_name + ", Ducky: " + ducky
    
roster = makeRoster("krewes.txt")

print(selectRandom(roster))
