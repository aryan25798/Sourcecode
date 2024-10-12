def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1  # Factorial of 0 or 1 is 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i  # Multiply result by each number up to n
        return result

# Test the function
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
