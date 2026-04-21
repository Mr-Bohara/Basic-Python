# ---------------------- Common Exceptions Examples ----------------------

# ValueError
# int('hello')

# ZeroDivisionError
# 10 / 0

# FileNotFoundError
# open('xyz.txt')

# IndexError
# lst = [32, 3, 2]
# lst[22]

# KeyError
# d = {'a': 1}
# d['z']

# TypeError
# 'hello' + 5

# AttributeError
# num = 33
# num.upper()


# ---------------------- File Handling with Exception ----------------------

try:
    filename = 'lll.txt'
    with open(filename, 'r') as f:
        content = f.read()

except FileNotFoundError:
    print('Error: file not found')

except PermissionError:
    print('Error: permission denied to read the file!')

else:
    print('File read successfully!')
    print(f'Content: {content[:100]} .....')

finally:
    print('File operation attempt complete.')


# ---------------------- Custom Exception Function ----------------------

def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f'Age must be an integer, got {type(age).__name__}')
    
    if age < 0 or age > 100:
        raise ValueError(f'Age {age} is not realistic (must be 0–100)')
    
    return age


# Testing custom exceptions
try:
    set_age(-5)
except ValueError as e:
    print(f'ValueError: {e}')

try:
    set_age('twenty')
except TypeError as e:
    print(f'TypeError: {e}')


# ---------------------- Input Validation Pattern ----------------------

print('____________________________________ Input Validation Pattern ____________________________________')

def get_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                print(f'Must be at least {min_val}. Try again.')
                continue

            if max_val is not None and value > max_val:
                print(f'Must be at most {max_val}. Try again.')
                continue

            return value

        except ValueError:
            print('Invalid input. Please enter a whole number.')


# ---------------------- Main Program ----------------------

if __name__ == "__main__":
    age = get_integer('Enter your age: ', 0, 100)
    score = get_integer('Enter your score: ', 0, 100)

    print(f'Age: {age}, Score: {score}')