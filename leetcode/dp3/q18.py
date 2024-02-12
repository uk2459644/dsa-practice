
def digit_sum(number):
    return sum(int(digit) for digit in str(number))

def sort_numbers_by_digit_sum(numbers):
    # Use a lambda function as the key for sorting
    sorted_numbers = sorted(numbers, key=lambda x: digit_sum(x),reverse=True)
    return sorted_numbers

# Example usage:
my_numbers = [123, 45, 789, 12, 567]
sorted_numbers = sort_numbers_by_digit_sum(my_numbers)

print("Original numbers:", my_numbers)
print("Sorted numbers by digit sum:", sorted_numbers)
