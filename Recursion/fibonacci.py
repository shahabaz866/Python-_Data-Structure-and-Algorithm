
#  Fibonacci ...

def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 

n = 6
print(f"The {n}th Fibonacci number is {fibonacci(n)}")

