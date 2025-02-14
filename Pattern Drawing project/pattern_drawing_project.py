# 🖼️ Python Pattern Drawing Project

stop_program = False

while True:

    # Step 1: Display a menu to the user
    print("\n\n\n🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5, 8]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        # TODO: Loop through rows and print increasing stars
        for i in range(rows + 1):
            print('*' * i)

    elif choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center
        print('*' * size)
        for k in range(size - 2):
            print('*' + (' ' * (size - 2)) + '*')
        print('*' * size)

    if choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops
        # Top half of the diamond (including middle row)
        for i in range(rows):
            # Print spaces for centering
            print(" " * (rows - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1))

        # Bottom half of the diamond
        for i in range(rows - 2, -1, -1):
            # Print spaces for centering
            print(" " * (rows - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1))

    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row
        for i in range(1, rows + 1):
            print('*' * ((rows + 1) - i))

    elif choice == 5:  # Hollow Square
        # TODO: Similar to choice 2 but ensure perfect square logic
        print('*' * size)
        for k in range(size - 2):
            print('*' + (' ' * (size - 2)) + '*')
        print('*' * size)

    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid
        # Top half of the diamond (including middle row)
        for i in range(rows):
            # Print spaces for centering
            print(" " * (rows - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1))

    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid
        # Bottom half of the diamond
        for i in range(rows - 1, -1, -1):
            # Print spaces for centering
            print(" " * (rows - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1))

    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

        print('*' * width)
        for i in range(height - 2):
            print('*' + ((width - 2) * ' ') + '*')
        print('*' * width)

    else:
        print("❌ Invalid choice! Please restart the program.")

    while True:
        print('\nDo you want to Restart the program or Exit?')
        command = input('Type Restart or Exit:\n')
        if command == 'Restart':
            break
        elif command == 'Exit':
            stop_program = True
            break
        else:
            continue

    if stop_program:
        break
