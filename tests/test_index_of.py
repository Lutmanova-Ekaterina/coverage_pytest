import pytest
from cproject.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0

def test2_index_of():
    assert index_of([], 10, 8) == -1
    assert index_of([10, 25, 30, 44, 50], 20, -10) == 3
    assert index_of([10, 25, 30, 44, 50], 1000) == -1