import pytest
from assignment import *

def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

assert format_string("John", 25) == "My name is John and I am 25 years old"
    

def conditional_check(num: int):
    if(num == 10):
        return f"Equal" 
    elif(num <= 10):
        return f"Lesser"
    else:
        return f"Greater"
    
assert conditional_check(15) == "Greater"
assert conditional_check(5) == "Lesser"
assert conditional_check(10) == "Equal"


def loop_sum(num: int):
    total = 0;
    for x in range(0, num + 1, 1):
        total += x;
    
    return total;  

assert loop_sum(5) == 15
assert loop_sum(3) == 6
assert loop_sum(1) == 1


def list_operations(numbers):
    if not numbers:
        return (0, None, None)
    return(sum(numbers), max(numbers), min(numbers))

assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)
assert list_operations([10, 20, 30]) == (60, 30, 10)


def dict_operations(dic):
    firstname = [];
    for key, values in dic.items():
        if(values > 75):
            firstname.append(key);
    return firstname
    

students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
result = dict_operations(students)
assert set(result) == {"John", "Alice", "Eve"}

def set_operations(*baskets):
    if not baskets:
        return set()
    result = set(baskets[0])
    for basket in baskets[1:]:
     temp = set()
     for item in basket:
        if(item in result):
            temp.add(item)

    return temp
    
assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}
assert set_operations([1, 2], [3, 4]) == set()

def arithmetic_ops(*numbs):
    temp = dict()
    summ = 0;
    difference = numbs[0];
    product = 1;
    quotient = numbs[0]
    result = {}

    for i,numb in enumerate(numbs):
        summ += numb;
        product *= numb;
        if(i>0):
            difference -= numb; 
            quotient /= numb;
        temp["sum"] = summ;
        temp["difference"] = difference;
        temp["product"] = product;
        temp["quotient"] = quotient;

    result = temp
    return result;


result = arithmetic_ops(10, 5)

assert result["sum"] == 15
assert result["difference"] == 5
assert result["product"] == 50
assert result["quotient"] == 2.0


def logical_ops(*signals):
    signal1 = bool
    signal2 = bool
    result = dict()
    
    signal1 = signals[0]
    signal2 = signals[1]

    result["and"] = (signal1 == True and signal2 == True)
    result["or"] = (signal1 == True or signal2 == True)
    result["not_x"] = not(signal1)

    return result

result = logical_ops(True, False)
assert result["and"] == False
assert result["or"] == True
assert result["not_x"] == False

def bitwise_ops(*inputs):
    input1 = inputs[0]
    input2 = inputs[1]
    bitwise_result = dict()
    bitwise_result["and"] = input1 & input2
    bitwise_result["or"] = input1 | input2
    bitwise_result["xor"] = input1 ^ input2
    return bitwise_result

result = bitwise_ops(12, 10)


assert result["and"] == 8
assert result["or"] == 14
assert result["xor"] == 6