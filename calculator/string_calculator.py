
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

    numbers_part = numbers_part.replace('\n',delimiter)
    numbers_string = re.split(delimiter,numbers_part)
    neagatives = []
    total = 0

    for num_str in numbers_string:
        if not num_str.strip():
            continue
        num = int (num_str)




