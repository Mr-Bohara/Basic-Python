f_name = 'your first name'
l_name = ' your last name'
age = 20
city = 'your city'
is_student = True
gpa = 2.4

print(f_name, l_name, age, city, is_student, gpa, sep=' - ')

birth_year = 2063
current_year = 2082
calculate_age = current_year - birth_year
print(calculate_age, "years old.")






print('------------------Simple calculater ----------------------')

f_num = '4'
s_num = '2'
first = int(f_num)
second = int(s_num)
addition = first + second
substraction = first - second
miltplication = first * second
if second != 0:
    divide = first - second
    print('divid', divide)
else:
    print('division by zero is not allowed!')

print('adde', addition)
print('sub', substraction)
print('multi', miltplication)




print("____________________________Logical operatos______________________________")
age = 2
income = 45000
is_citizen = True

can_vote = (age >= 18) and (is_citizen == True)
if can_vote == True:
    print("Can vote.")
else:
    print("cannot vote")

gets_discount = (age < 18 ) or (age > 80)
if gets_discount == True:
    print("Get Discount ", gets_discount)
else:
    print("he is adult.")

is_minor = not (age > 18)
if is_minor == True:
    print("He is minor.")
else:
    print("He is not minor.")

loan_approved = (income > 30000) and is_citizen == True and not(age < 21 )
if loan_approved == True:
    print("Get loan approved.")
else:
    print("not loan approved.")





print("______________________________positive or nagitave number______________________________")
n = 0
if n > 0:
    print('positive')
    if n%2 == 0:
        print("It is also even")
    else:
        print("odd")
elif n < 0:
    print("negative")
elif n == 0:
    print("it is zero")
else:
    print("invalid")


print("______________________Mark sheet ___________________")

score = 100
student_name = 'Ram'
# Input validation
if score < 0 or score > 100 :
    print("Invalid score! Must be between 0 and 100.")
else:
    # Determine grade and status
    if score >= 90:
        grade = "A+"
        remark = "Outstanding!"
        status = "PASS"
    elif score >= 80:
        grade = "A"
        remark = "Excellent!"
        status = "PASS"
    elif score >= 70:
        grade = "B"
        remark = "Very Good"
        status = "PASS"
    elif score >= 60:
        grade = "C"
        remark = "Good"
        status = "PASS"
    elif score >= 50:
        grade = "D"
        remark = "Needs Improvement"
        status = "PASS"
    else:
        grade = "F"
        remark = "Please Retake"
print(f"Student: {student_name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print(f"Status: {status}")




print("____________________IMPORT_____________________")

import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(3.3))
print(math.factorial(5))
print(4**2)

import math as m
print(m.sqrt(6))

print("Random")
import random as r
print(int(r.randint(1,100)))
print(int(r.random()))

color = [ 'rad', 'blue', 'green', 'yellow']
print(r.choice(color))

print("___________________________Date Time___________________________")

from datetime import datetime, date
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)


print('_____________________________File Handling________________________________')


with open('note.txt', 'w') as file:
    file.write('Good Mornning!\n')

file = open('note.txt', 'w')
file.write('Hello, File\n')
file.close()

with open('note.txt', 'w') as f:
    f.write('Dear Diary,\n')
    f.write('Today, I learned python file handling.\n')
    f.write('It is easier than I expected!\n')

with open('note.txt', 'a') as f:
    f.write('And now i know how to append to files!\n')

files = open('note.txt', 'a')
files.write('Alice, 90\nBob, 28\n')
files.close()

with open('note.txt', 'r') as f:
    content = f.read()
    print('Today' in content)
    print(content)

    lines = f.readlines()
    for line in lines:
        print(line.strip())
  
    for line in f:
        name, score = line.strip().split(',')
        print(f'{name}: {score}')