def countDigitOne(n):
    # Initialize the count of digit '1' occurrences
    count = 0
    
    # Initialize the factor to 1, representing the current position (units, tens, hundreds, etc.)
    factor = 1

    # Continue until the factor exceeds n
    while factor <= n:
        # Calculate the divisor for the current position
        divisor = factor * 10

        # Calculate the number of full cycles completed at the current position
        fullCycles = n // divisor

        # Calculate the remaining digits after the full cycles
        remainingDigits = n % divisor

        # Calculate the count for the current position
        count += fullCycles * factor + min(max(remainingDigits - factor + 1, 0), factor)

        # Move to the next position
        factor *= 10

    # Return the final count
    return count

# Example usage:
n = int(input())
result = countDigitOne(n)
print(result)
