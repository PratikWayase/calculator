
import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = "."
    numbers_part = numbers

    if numbers.startswith('//'):
        delimeter_line , numbers_part = numbers.split('\n',1)
        delimiter = delimeter_line[2:]
        delimiter = re.escape(delimiter)


