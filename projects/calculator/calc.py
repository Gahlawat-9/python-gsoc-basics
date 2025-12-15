def add(a, b):
    return a + b

def sub(a, b):
    return a - b

while True:
    print("\n1. Add\n2. Subtract\n3. Exit")
    choice = input("Choose: ")

    if choice == "3":
        break

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", sub(a, b))
