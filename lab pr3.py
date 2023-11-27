def isHappy(n):
    def get_next(num):
        # Helper function to calculate the sum of squares of digits
        result = 0
        while num > 0:
            digit = num % 10
            result += digit ** 2
            num //= 10
        return result

    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next(n)

    return n == 1

# Example usage:
number = 19
result = isHappy(number)
print(result)
