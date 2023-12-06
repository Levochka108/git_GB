
def multiplication(x: int | float , y: int | float):
    result = x * y
    return result

def division(x: int | float, y: int | float):
    result = x / y
    return result

def subtraction(x: int, y: int):
    result = x - y
    return result
def printer():
    print(f"Произведино умножение {multiplication(5, 5)} ")
    print(f"Проиведино умножение {multiplication(2.25, 5.5)}")
    print(f"Произведино деление {division(25, 5)}")

    print(f"Произведино вычитание {subtraction(10, 5)}")

if __name__ == '__main__':
    printer()
