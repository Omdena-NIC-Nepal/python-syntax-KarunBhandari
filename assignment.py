def format_string(name:str, age:int):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if(number == 10):
        return f"Equal" 
    elif(number <= 10):
        return f"Lesser"
    else:
        return f"Greater"

def loop_sum(n:int):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0;
    for x in range(0, n + 1, 1):
        total += x;
    
    return total;

def list_operations(numbers:list):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return (0, None, None)
    return(sum(numbers), max(numbers), min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    firstname = [];
    for key, values in students_dict.items():
        if(values > 75):
            firstname.append(key);
    return firstname

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    if not list1 and not list2:
        return set()
    result = set(list1)
    temp = set()
    for item in list2:
     if(item in result):
        temp.add(item)
    return temp
print(set_operations([1, 2, 3], [2, 3, 4]))
    

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    temp = dict()
    result = {}

    #for i,numb in enumerate(numbs):
    summ = a+b;
    product = a*b;
    difference = a-b; 
    quotient = a/b;
    temp["sum"] = summ;
    temp["difference"] = difference;
    temp["product"] = product;
    temp["quotient"] = quotient;

    result = temp
    return result;

def logical_ops(x:bool, y:bool):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    result = dict()

    result["and"] = (x == True and y == True)
    result["or"] = (x == True or y == True)
    result["not_x"] = not(x)

    return result

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    bitwise_result = dict()
    bitwise_result["and"] = a & b
    bitwise_result["or"] = a | b
    bitwise_result["xor"] = a ^ b
    return bitwise_result

