def process_number(number):
    # Function to process a number: 1) if the number is even, it should return half the number. 2) if the number is odd, it should return three times the number plus one.
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number
