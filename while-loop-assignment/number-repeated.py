rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i):        # Inner loop for printing numbers
        print(i, end="")     # Print the row number, separated by spaces
    print()                   # Move to the next line
