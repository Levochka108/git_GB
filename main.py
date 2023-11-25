def func(x: int | float , y: int | float):
    result = x * y
    return result

def printer():
    print(f"{func(5, 5)} ")
    print(f"{func(2.25, 5.5)}")

if __name__ == '__main__':
    printer()