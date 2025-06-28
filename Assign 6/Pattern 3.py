def pyramid_pattern(n):
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end="")
        # Print stars
        print('*' * (2 * i + 1))
    print()

