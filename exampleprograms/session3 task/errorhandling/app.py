
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def process_data(data):
    try:
        result = data * 2
        logging.info(f"Processed data: {data}")
        return result
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return None

# Example usage:
print(process_data(5))  # Output: 10
print(process_data('string'))  # Output: None, and logs an error to 'app.log'

