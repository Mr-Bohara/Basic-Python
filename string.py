# Chapter 6-  Strings

txt = "  Hello, Dhnaush Bohara    "
print("case methods")
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.swapcase())

print("white space methods")
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

print("search methods")
print(txt.find('bohara'))
print(txt.count('a'))
print(txt.startswith('Hello'))
print("Dhanush" in txt)

print("Modification methods")
print(txt.replace("Bohara", "Xettry"))

print("split and join")
tt = txt.split(",")
print(tt)
rejoined = '|'.join(tt)
print(rejoined)

print("check content")
print('123'.isdigit())
print('abc'.isalpha())
print('12ssa'.isalnum())
print(' '.isspace())


print("Mini projrct- Password strengh checker")

password = 'hell87632Dahaopy'

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
is_long = len(password)>=8

print(f"Length: {len(password)} chars {'OK' if is_long else 'Too short'}")
print(f"Uppercase: {'Yes' if has_upper else 'No'}")
print(f"Lowercase: {'Yes' if has_lower else 'No'}")

score = sum([has_lower, has_upper, is_long])

if score == 5:
    print("Strong password")
elif score >= 3:
    print("Medium password")
else:
    print("week password")