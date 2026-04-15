coorrdinates = (50.33, -76.4321)
pgb_color = (255, 123, 0)
person = ("Anil", 43, "Engineer")

print(coorrdinates)
print(coorrdinates[-1])
print(len(person))

print("_____________SET_________________")

fruit = {"banana", 'cherry', 'apple'}
number = [34,55,32,21]
nums = set(number)
num = {22,34,23,13,56,43,43,4,34,32,43,4,2,4,2,4}
print(fruit)
print(num)
print(type(nums), nums)


print("\n____________DECTIONARYS_____________________")
student = {
    'name': 'Dhansuh', 'age': 32, 'grade': [32.3, 32.2, 21.2], 'is_erolled': True
}
print(student)
print(student['name'])
print(student['age'])
student['age'] = 90
student['email'] = 'dhnaushboahara@mail.com'
print(student['email'])

del student['is_erolled']
removed = student.pop('email')
print(student.keys())
print(list(student.items()))



print("____________MINI PROJECT_________________")

gradebook ={}

while True:
    print("\n1. add student 2. add grade 3. view report 4. exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter srudent name: ")
        gradebook[name] = []
        print(f"{name} added.")

    elif choice == "2":
        name = input("enter student name: ")
        if name in gradebook:
            grade = float(input("Grade: "))
            gradebook[name].append(grade)
            print(F"grade  {grade} added for {name}")
        else:
            print('student not found. please try again...')
        
    elif choice == '3':
        print("_________print grade repor_____")

        for student, grades in gradebook.items():
            if grades:
                avg = sum(grades)/ len(grades)
                print(F"{student}: grades: {grades} and avarage: {avg}")
            else:
                print('not grade yet.')
            
    elif choice == "4":
        print("Exit")
        break

    else:
        print("pLease valid number choice 1 to 4.")