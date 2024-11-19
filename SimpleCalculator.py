# Simple Calculator Program  

def calculator():  
    # Prompt the user for the first number  
    num1 = float(input("Enter the first number: "))  
    
    # Prompt the user for the second number  
    num2 = float(input("Enter the second number: "))  
    
    # Prompt the user for the operation they want to perform  
    operation = input("Enter the operation (+, -, *, /): ")  

    # Perform the calculation based on the input operator  
    if operation == '+':  
        result = num1 + num2  # Addition  
    elif operation == '-':  
        result = num1 - num2  # Subtraction  
    elif operation == '*':  
        result = num1 * num2  # Multiplication  
    elif operation == '/':  
        if num2 != 0:  # Check for division by zero  
            result = num1 / num2  # Division  
        else:  
            return "Error: Division by zero is not allowed."  
    else:  
        return "Error: Invalid operation."  

    # Return the result of the calculation  
    return f"The result of {num1} {operation} {num2} = {result}"  

# Call the calculator function and print the result  
print(calculator())