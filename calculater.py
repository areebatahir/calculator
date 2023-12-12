def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
            raise ValueError("Can not divided by Zero.")
    return x/y
def calculator():
    print("Simple Calculator")
    print("Enter Your Choice")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter Your Choice (1/2/3/4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid Choice. Please select a valid choice.")
        return
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid Choice, Please Enter a numeric digit.")
        return
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        try:
            result = division(num1, num2)
        except ValueError as e:
                print(e)
                return
        operation = '/'
    print(f"{num1} {operation} {num2} = {result}")
if __name__ == '__main__':
    calculator()


