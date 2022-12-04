import pytest
from cproject.get import get

def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"

def test2_get():
    assert get([10, 25, 38, 487, 1000], 12, 8) == 8
    assert get([10, 25, 38, 487, 1000], -12, 8) == 8

def test3_get():
    assert get([5, 10, 45, 5, 80], -1) == None
    assert get([5, 10, 45, 5, 80], 30) == None
