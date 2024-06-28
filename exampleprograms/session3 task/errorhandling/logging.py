#: Error Handling and Debugging
#•	Objective: Implement error handling and logging.
#•	Tasks:
#1.	Use try and except blocks to handle potential errors.
#2.	Implement assertions to validate function inputs.
#3.	Use logging to track the application’s execution and errors.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operation, check your input types!")
    else:
        return result
    finally:
        print("Execution completed.")

# Example usage:
print(divide(10, 2))
print(divide(10, 0))


def calculate_area(length, width):
    assert length > 0 and width > 0, "Dimensions must be positive"
    return length * width

# Example usage:
print(calculate_area(5, 4))
print(calculate_area(-1, 4))


