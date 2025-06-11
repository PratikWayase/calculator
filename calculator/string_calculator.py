import re

def add(numbers: str) -> int:
    if not numbers.strip():
        return 0

    delimiter = "," 
    numbers_part = numbers 

    if numbers.startswith('//'):
        delimiter_line, numbers_part = numbers.split('\n', 1)
        delimiter = delimiter_line[2:]
        delimiter = re.escape(delimiter)

    numbers_part = numbers_part.replace('\n', delimiter)

    numbers_list = re.split(delimiter, numbers_part)
    
    negatives = [] 
    total = 0 

    for num_str in numbers_list:
        if not num_str.strip():
            continue
        
        num = int(num_str) 

        if num < 0:
            negatives.append(str(num)) 
        else:
           
            total += num

    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
        
    return total 





