def greet(name):
    print(f"Hello, {name}!")  

def goldilocks(bed_length):
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")  


def square_list(numbers):
    return [num ** 2 for num in numbers]  

print(square_list([1, 2, 3, 4, 5]))


def fibonacci_stop(max_value):
    fib_sequence = [1, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value >= max_value:
            break
        fib_sequence.append(next_value)
    return fib_sequence


def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_angles.append(-999)  
        else:
            cleaned_angles.append(angle)  
    return cleaned_angles


print(greet("Alice"))  
print(fibonacci_stop(100))  
print(clean_pitch([10, -5, 95, 45], [1, 1, 0, 1])) 
