#: Error Handling and Debugging
#•	Objective: Implement error handling and logging.
#•	Tasks:
#1.	Use try and except blocks to handle potential errors.
#2.	Implement assertions to validate function inputs.
#3.	Use logging to track the application’s execution and errors.
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data):
    try:
        # Process data
        result = data / 0  # Example: division by zero
    except Exception as e:
        logging.error(f"Error processing data: {str(e)}")

# Example usage
data = 100
process_data(data)