import pytest
from cproject.slice import my_slice

def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]

def test2_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 10, 5) == []
    assert my_slice([], 10, 5) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -10, 5) == [1, 2, 3, 4]

def test3_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], -4, 4) == [3, 4]
    assert my_slice([1, 2, 3, 4, 5, 6], -4) == [3, 4, 5, 6]