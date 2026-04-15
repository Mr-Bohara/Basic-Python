coff_name = 'Latte'
price = 3.4
quantity = 20
print(f'Item: {coff_name}')
print(f'price: ${price}')
print(f'Total value: ${price * quantity}')

print('_______________Pizza__________________')

small_pizza = 7.55
large_pizza = 9.99

small_qty = 3
large_qty = 4

subtotlal = (small_pizza * small_qty) + (large_pizza * large_qty)
tax = subtotlal * 0.88
total = subtotlal = tax

print(f'suntotal: ${subtotlal:.2f}')
print(f'Tax: 8%: ${tax:.2f}')
print(f'Tatal: ${total:.3f}')

if total > 90:
    print("You get free soda!")



print('_________________________________Grade Evaluator_________________________________')

score = 70

if score < 0 or score > 100:
    print("Please enter score range in 1 to 100")
else:
    if score >= 90:
        grade = 'A'
        sms = "Excellent"
    elif score >= 60:
        grade = "B"
        sms = 'Good'
    elif score >= 40:
        grade = 'C'
        sms = 'Need to Improve'
    else:
        grade = 'F'
        sms = 'See your teacher'
  
    print("Your Grade is ", grade)
    print('Your sms is ', sms)

    if score > 40:
        print('pass ', score)
    else:
        print('Fail ', score)


print('______________________________ATM Machine________________________________')

balance = 1000
pin = 1234
attempt = 0
max_atm = 2

while True:
    entered_pin = 1234
    if entered_pin == pin:
        print('Login Successful!')
        print(f'Your balance is {balance}')

        amount = 23.33

        if amount <= 0:
            print('Invalid amoun Please try again', amount)
        elif amount > balance:
            print('Insufficient balance Please try again', amount)
        else:
            balance -= amount
            print(f'withdrawn: ${amount}')
            print(f'remaining balance is ${balance}')
            break;
    else:
        print('Wrong PIN Please try again!')
        attempt += 1
        if attempt == max_atm:
            print('Too many failed attempts. Your account is locked.')
        break;



print('___________________________Health Screening System____________________________')

weight = 60
height = 5.6

bmi = weight / (height**2)
print(f'Your BIM:{bmi:.2f}')

if bmi < 18.5:
    category = 'underweight'
    advice = 'Eat more nutritious food'
elif bmi < 25:
    category = 'overweight'
    advice = 'consider regular execise'
elif bmi < 30:
    category = 'obese'
    advice = 'Your are dth'
else:
    category ='obese'
    advice = 'consult a doctor'

print(category, 'and', advice)



print('__________________________________Gussing Number____________________________')

import random

print('Guess the number (1 to 15)')

secret = random.randint(1, 15)
attempt = 0
max_atm = 2

while True:
    guess = 11
    attempt += 1

    if guess < 1 or guess > 15:
        sms = 'Out of range! Please guess between 1 and 15.'
    elif guess < secret:
        sms = 'Too low!'
    elif guess > secret:
        sms = 'Too high!'
    else:
        print('Correct guess! ')
        break

    print(sms)

    if attempt == max_atm:
        print(f"Game over! The correct number was {secret}")
        break


print('___________________________String_________________________________')
print('SignUp form')

username = 'name123'
errors = []

if len(username)< 5:
    errors.append('Too short mininum 5 char' )
if len(username) > 10:
    errors.append('too long')
if not username[0].isalpha():
    errors.append('must be start with a letter')
if ' ' in username:
    errors.append('cannot cotain space')
if not username.isalnum():
    errors.append('only letters adn number allowed')

if errors:
    print('invalid username')
    for error in errors:
        print(error)
else:
    print(username)
    print(len(username))
    print(username.upper())