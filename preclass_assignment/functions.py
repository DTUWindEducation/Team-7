#specify the numbers that the user will give
def get_numbers():
    user_input = input("Enter numbers separated by spaces: ")  
    numbers = [int(num) for num in user_input.split()]  
    return numbers  

numbers = get_numbers()

#make th
def square_list(numbers):
    squared_numbers = []  # Create an empty list to store the values from before
    for num in numbers:
        squared_numbers.append(num ** 2)  # Square each number and add it to the list
    return squared_numbers

print(square_list(numbers))

###
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

####

def goldilocks(bed_length):
    if bed_length < 140:
        print("The bed is too small. Goldilocks is unhappy!")
    elif bed_length > 150:
        print("The bed is too large. Goldilocks is unhappy!")
    else:
        print("The bed is just right. Goldilocks is happy!")

bed_length = int(input("bed_lenght is (cm): "))
goldilocks(bed_length)

####

name = str(input("the name is: "))
def greet ():
    print (f"Hello, {name}!")
greet()


###


def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []  # List to store cleaned values

    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_angles.append(-999)  # Mark bad values
        else:
            cleaned_angles.append(pitch)  # Keep good values unchanged

    return cleaned_angles

# Example usage:
pitch_angles = [10, 85, -5, 95, 40, 100, 70]
status_signals = [0, 0, 1, 0, 0, 2, 1]  # 1 or greater indicates a malfunction


cleaned_data = clean_pitch(pitch_angles, status_signals)
print(cleaned_data)  