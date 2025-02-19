def fibonacci_stop(max_value):
    if max_value < 1:
        return []  # Return an empty list if max_value is less than 1

    fibonacci_numbers = [1, 1]  # Start with the first two Fibonacci numbers

    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Sum of last two numbers
        if next_fib > max_value:  # Stop if the next number exceeds max_value
            break
        fibonacci_numbers.append(next_fib)  # Add the next Fibonacci number to the list

    return fibonacci_numbers


max_value = int(input("Enter the maximum value for Fibonacci sequence: "))
print(fibonacci_stop(max_value))
