import pytest
from assignment import *

def test_format_string():
    assert format_string("John", 25) == "My name is John and I am 25 years old"
    assert format_string("Alice", 30) == "My name is Alice and I am 30 years old"
    

def test_conditional_check():
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"


def test_loop_sum():
    assert loop_sum(5) == 15
    assert loop_sum(3) == 6
    assert loop_sum(1) == 1


def test_list_operations():
    assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)
    assert list_operations([10, 20, 30]) == (60, 30, 10)


def test_dict_operations():
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    result = dict_operations(students)
    assert set(result) == {"John", "Alice", "Eve"}

def test_set_operations():
    assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert set_operations([1, 2], [3, 4]) == set()

def test_arithmetic_ops():
    result = arithmetic_ops(10, 5)
    assert result["sum"] == 15
    assert result["difference"] == 5
    assert result["product"] == 50
    assert result["quotient"] == 2.0


def test_logical_ops():
    result = logical_ops(True, False)
    assert result["and"] == False
    assert result["or"] == True
    assert result["not_x"] == False

def test_bitwise_ops():
    result = bitwise_ops(12, 10)
    assert result["and"] == 8
    assert result["or"] == 14
    assert result["xor"] == 6   