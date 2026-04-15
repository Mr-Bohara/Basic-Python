fruit = ['apple', 'banana', 'cherry', 'date', 'tiger', 'nepal', 'google', 'Techspire college']
num = [12,33,21,21,34,5,5,5,4,3,4,21,22,22,21]
mixed = ['sarita dhami', 'prem dhami', 23, 22, True, False, 2.1, 2.3]
empty = []

print(fruit)
print(fruit[4])
print(fruit[-2])

print("2:6 ", fruit[2:6])
print(fruit[:4])
print(fruit[4:])

fruit.insert(1, 'Dog')
fruit.remove('Dog')
print(fruit)
print("pop", fruit.pop(4))
print('count', num.count(4))
print(sorted(num))
print("______________________")

score = num

for s in score:
    print(s, end='')

for p, s in enumerate(score):
    print(f"\nstudent {p + 1 }: {s}")

s = num
print(f"heighest: {max(s)}")
print(f"lowest: {min(s)}")
print(f"total: {sum(s)}")
print(f"Avarage: {sum(s)/len(s)}")


passing = 0
for s in score:
    if s >=80:
        passing += 1

print(F"passing: {passing}/{len(score)}")

print("_________________________")
print('list of comprehension')

square =[]

for i in range(1, 8):
    square.append(i**2)
print(square)
square = [i**2 for i in range(1, 8)]

word = ['hello', 'nepal', 'kathmandu']
upper = []
for w in word:
    upper.append(w.upper())
print(upper)
uppeer= [w.upper() for w in word]
print(uppeer)

print("____________________________")
print("mini project")

cart = []
price = {}
while True:
    print("\n1. add item. 2. remove item. 3. view cart. 4. checkout 5. Exit")
    choice = input("Enter your choice")

    if choice  == '1':
        item = input("Enter Item Name: ")
        prices = float(input("Enter price: "))
        cart.append(item)
        price[item] = prices
        print(f"{item} added to cart!")

    elif choice == "2":
        item = input("Enter remove which item?")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed.")
        else:
            print(f"item not in cart, please try again...")
        
    elif choice == '3':
        if cart:
            print("\nYour cart")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item} -$(price[item]")
            else:
                print("Cart is Empty.")
        
    elif choice == "5":
        total = sum(price[item] for item in cart)
        print(total)
        break

    elif choice == "6":
        print("Exit")
        break
    else:
        print('please enter valid num range 1 to 6.')