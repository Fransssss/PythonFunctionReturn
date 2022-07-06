# function return
#=================================

def add(numO, numT):
    return (numO + numT)

def sub(numO, numT):
    return numO - numT

def mul(numO, numT):
    return numO * numT

def div(numO, numT):
    return numO / numT

def mod(numO, numT):
    return numO % numT

#=================================

print("\n== Basic Mathematical Operations ==")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Module")
print("E. Exit")
choice = input("choice: ")

while choice != 'E' and choice != 'e':
    if choice == '1':
        print("\nAddition")
        print("input 1st number: ")
        num_one = int(input())
        print("input 2nd number: ")
        num_two = int(input())
        rs = add(num_one, num_two)
        print("[ " + str(num_one) + " + " + str(num_two) + " = " + str(rs) + " ]")

    elif choice == '2':
        print("\nSubtraction")
        print("input 1st number: ")
        num_one = int(input())
        print("input 2nd number: ")
        num_two = int(input())
        rs = sub(num_one, num_two)
        print("[ " + str(num_one) + " - " + str(num_two) + " = " + str(rs) + " ]")

    elif choice == '3':
        print("\nMultiplication")
        print("input 1st number: ")
        num_one = int(input())
        print("input 2nd number: ")
        num_two = int(input())
        rs = mul(num_one, num_two)
        print("[ " + str(num_one) + " x " + str(num_two) + " = " + str(rs) + " ]")

    elif choice == '4':
        print("\nDivision")
        print("input 1st number: ")
        num_one = int(input())
        print("input 2nd number: ")
        num_two = int(input())
        rs = div(num_one, num_two)
        print("[ " + str(num_one) + " / " + str(num_two) + " = " + str(rs) + " ]")

    elif choice == '5':
        print("\nModule")
        print("input 1st number: ")
        num_one = int(input())
        print("input 2nd number: ")
        num_two = int(input())
        rs = mod(num_one, num_two)
        print("[ " + str(num_one) + " % " + str(num_two) + " = " + str(rs) + " ]")

    else:
        print("\nInvalid input")

    print("\n== Basic Mathematical Operations ==")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Module")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")