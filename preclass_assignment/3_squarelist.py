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