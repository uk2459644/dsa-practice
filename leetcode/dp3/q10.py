def generate_numbers(n):
    if n <= 0:
        return []

    result = [1]
    i2, i3, i5 = 0, 0, 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    while len(result) < n:
        next_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        result.append(next_number)

        if next_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = result[i2] * 2

        if next_number == next_multiple_of_3:
            
            i3 += 1
            next_multiple_of_3 = result[i3] * 3

        if next_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = result[i5] * 5

    return result

# Example: Generate the first 10 numbers
generated_numbers = generate_numbers(10)
print(generated_numbers,generated_numbers[-1])
