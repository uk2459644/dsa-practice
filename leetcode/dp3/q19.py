def arrange_digits_in_ascending_order(n):
    # Convert the number to a string to work with individual digits
    num_str = str(n)
    
    # Extract and sort the digits in ascending order
    sorted_digits = sorted(num_str)
    
    # Ensure the first element is the minimum of the digits (except zero)
    if '0' in sorted_digits:
        # Move '0' to the beginning if present
        sorted_digits.remove('0')
        sorted_digits.insert(0, '0')
    else:
        # Swap the first and minimum element
        min_index = sorted_digits.index(min(sorted_digits))
        sorted_digits[0], sorted_digits[min_index] = sorted_digits[min_index], sorted_digits[0]
    
    # Join the sorted digits and convert back to an integer
    result = int(''.join(sorted_digits))
    
    return sorted_digits

# Example usage:
number = 305172
result = arrange_digits_in_ascending_order(number)
print(f"The original number: {number}")
print(f"The arranged number in ascending order: {result}")
