# Alex Luo
# TummyAKE
# SoftDev
# Python Dictionaries and Random Selection
# Writing a function to randomly select a student from a dictionary where the keys are periods and the values are rosters.

# 2024-09-13
# Time: 10 minutes

import random

def func(krewes):
    x = random.randrange(0, len(krewes))
    pd = list(krewes.keys())[x]
    students = krewes[pd]
    x = random.randrange(0, len(students))
    student = students[x]
    return student

krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }
print (func(krewes))

