def print_butterfly(n):
    # Top half of the butterfly
    for i in range(1, n + 1):
        # Print stars on the left wing
        print("*" * i, end="")
        # Print spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Print stars on the right wing
        print("*" * i)
    
    # Bottom half of the butterfly
    for i in range(n, 0, -1):
        # Print stars on the left wing
        print("*" * i, end="")
        # Print spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Print stars on the right wing
        print("*" * i)

# Example usage
rows = 5  # You can change the number of rows as needed
print_butterfly(rows)
