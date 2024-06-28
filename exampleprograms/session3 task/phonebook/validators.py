import re
import os
from dotenv import load_dotenv

load_dotenv()

phone_number_pattern = os.getenv("PHONE_NUMBER_PATTERN")

def is_valid_phone_number(phone_number):
    pattern = re.compile(phone_number_pattern)
    return pattern.match(phone_number) is not None
