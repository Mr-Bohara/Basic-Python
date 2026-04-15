x= 2.2
_y = float(2.2)
Z = int(2.2)
print(type(x))
print(type(_y))
print(type(Z))  

car = [[22.2, 22, 33, 22], [2, 5, 3, 4]]
total = 0
for i in car:
    pass
print(len(car))
print(i)

amount = 64.3
if amount >= 500:
    discount = 0.20
elif amount >= 200:
    discount = 0.10
else:
    discount = 0.05

discount_amount = amount * discount
final_amount = amount - discount_amount

print("Discount:", discount_amount)
print("Final bill:", final_amount)

start = int(input("Enter first number: "))  
end = int(input("Enter second number: "))
print("congratulations" +   str(int(end)-int(start)))