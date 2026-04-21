f = open('note.txt', 'r')

data = f.read(8)
line = f.readline()
f.close()

with open('students.txt', 'r') as f:
    content = f.read()
    f.seek(0)   # go back to start
    lines = f.readlines()

    for line in lines:
        print(line.strip())


student = [
    ('alisha', 90, 'A'),
    ('Babin', 98, 'B'),
    ('Sunil', 78, 'C'),
    ('Babita', 77, 'C')
]
with open('students.txt', 'w') as p:
    p.write('name, score, grade\n')
    for name, score, grade in student:
        p.write(f'{name}, {score}, {grade}\n')

print('------Report------')
with open('students.txt', 'r') as s:
    header = s.readline()
    for line in s:
        parts= line.strip().split(',')
        name, score, grade = parts
        print(f'{name}: {score}/100 (grade: {grade})')


print('________________________Existence and Error Handling____________________________')
import os

filename = 'notse.txt'
if os.path.exists(filename):
    with open(filename, 'r') as n:
        data = n.read() 
        print(data)
else:
    print(f'{filename} does not exist!')

try:
    with open('studensts.txt', 'r') as t:
        data = t.read()
        print(data)
except FileNotFoundError:
    print('File not Found!')
except PermissionError:
    print('No permission to read this file!')




print('___________________________________________________Personal Diary__________________________________________________')
from datetime import datetime
import os

daiary_file = 'My_dairy.txt'
def write_entery(entry):
    timestamp = datetime.now().strftime('%Y-%d %H:%M')
    with open(daiary_file, 'a+') as f:
        f.write(f'\n[{timestamp}]\n{entry}\n')
    print('Entery Saved')
    

def read_diary():
    if not os.path.exists(daiary_file):
        print('No diary enteries yet.')
        return
    
    with open(daiary_file, 'r') as f:
        print(f.read())

def count_enteries():
    if not os.path.exists(daiary_file): return 0
    with open(daiary_file, 'r') as f:
        return f.read().count(('[20]'))


print('My Personal Diary')
while True:
    print(f'\nEnteries so far: {count_enteries()}')
    print('''
          \n1. Write entry 
          \n2. Read all  
          \n3. Exit
          ''')
    choice = input('>>>>>')
    if choice == '1':
        entry = input('Write your thoughts:\n')
        write_entery(entry)
    elif choice == '2':
        read_diary
    elif choice == '3':
        print('Exit')
        break
    else:
        print('Invalid input please entery again 1,2 or 3. Try again')