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