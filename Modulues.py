import math as m

print(m.pi)
print(m.sqrt(20))
print(m.floor(3.2))
print(m.ceil(3.2))
print(m.factorial(7))

from math import  sqrt, pi, floor, factorial

print(sqrt(20))
print(floor(3.2))
print(factorial(7))

from math import *

print(cos(90))
print(sin(0))


print('___________________________________Random___________________________________')

import random

print(random.randint(1,10), 'This is random')

print(random.random(), 'random float between 0.0 to 1.0')

color = ['REd', 'blue', 'green']
print(random.choice(color), 'random color print')

num = [1,4,2,4,2,3,5,3,2,3,2,3]
print(random.shuffle(num), 'print shuffle function')
print(random.sample(num, 3), 'print sample function')



print('______________________________________Date Time Import___________________________________')

from datetime import datetime, date, timedelta
now = datetime.now()

print('print current time', now)
print(now.year)
print(now.month)
print(now.day)
#print(now.strfime('%B %D, %Y'))



print('_______________________________OS IMPORT __________________________________')

import os
print(os.getcwd(), ' || get current working directory.')
print(os.listdir('.'), ' || list of files on thi dir')
print(os.path.exists('test.py'), ' || is test.py file is exists print true or false. ')

print('_______________________________________Daily Planner ______________________________________')
from datetime import datetime, date
import random 
motivational_quotes = ['The secret of getting ahead gettting stared.',
                       "Belive you can and you're halfway there.",
                       'Success is not final, failure is not fatal.',
                       'The future blongs to those who belive in their deams.']

task = []
def show_header():
    now= datetime.now()
    print('___________________________________')
    print('Daily Planner')
    print(f"{now.strftime('%A, %B %d, %Y $H:%M')}")
    print(f"Quote: {random.choise(motivational_quotes)}")
    print()

show_header()

while True:
    print(F"1. add 2.View tasks 3.mark down 4.Exit")
    choice = input(">>>")

    if choice == '1':
        tasks = input("New task: ")
        time = input("Due time (eg. 3:00 PM): ")
        task.append({'task': task, 'time': time, 'done': False})
        print('task added')
    
    elif choice == '2':
        if not tasks:
            print("No tasks yet!")
        for i, t in enumerate(tasks, 1):
            status = '✓' if t['done'] else '○'
            print(f" {status} [{i}] {t['time']} - {t['task']}")
    
    elif choice == '3':
        num = int(input("Task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]['done'] = True
            print("Marked as done!")
    
    elif choice == '4':
        completed = sum(1 for t in tasks if t['done'])
        print(f"Session complete! {completed}/{len(tasks)} tasks done.")
        break