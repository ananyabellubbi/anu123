a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swaping: ")
print("first number =", a)
print("second number =", b)

a, b = b, a

print("After swaping: ")
print("first number =", a)
print("second number =", b)