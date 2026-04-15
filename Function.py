def greet(name):
    print("Hello, " + name + "!")
greet("Dhanush")
greet("Sunil")

def cal_area(lenght, width):
    area = lenght * width
    print(area)

cal_area(22, 53)
cal_area(2, 4)

def add(a, b):
    result = a + b
    return result
sum_result = add(3,4)
print(sum_result)
print(add(43,432))

def get_min_max(number):
    return min(number), max(number)
lowest, height = get_min_max([2,3,4,5,6,4,3,2,4,53,4,3,545,32,2,1])
print(lowest)
print(height)

print("_____________DEFAULT PARAMETERS______________")

def defaults(name, greeting="Hello", sms="Good Morning!"):
    print(greeting, "MR.", name, sms)
defaults('Dhanush')



counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
increment()
print(counter)


print("________________MINI PROJECT________________")

def add(a, b): return a+b
def substract(a, b): return a -b
def multiply(a, b): a*b
def divid(a,b):
    if b == 0:
        return 'Error'
    return a/b
def power(a, b): return a**b
def modulo(a, b): return a%b

def get_operation():
    ops = {'1':'+', '2':'-', '3':'*', '4':'/', '5':'**', '6':"%"}
    print(f"Operation: 1. add 2. sub 3. mul 4. devid 5.power 6. modulo")
    choice = input("choice (1-6): ")
    return ops.get(choice, None)

def calculate(a, op, b):
    operations = {'+': add, '-': substract, '*': multiply, '/': divid, '**': power, '%': modulo}
    if op in operations:
        return operations[op](a, b)
    return 'Invalid opration'

while True:
    try:
        num1 = float(input("Enter First number: "))
        op = get_operation()
        num2 = float(input("Enetr second number: "))
        result = calculate(num1, op, num2)
        print(f"Result: {num1} {op} {num2}")
   
    except ValueError:
        print("please enter valid number")
    if input("calcuate again? (y/n): ")!= 'y':
        break