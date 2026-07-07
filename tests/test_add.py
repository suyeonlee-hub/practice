import pytest
from typing import Union

from main import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),
        (5.5, 2.3, 7.8),
        (5, 2.3, 7.3),
        (0, 0, 0),
        (-1, 1, 0),

    ]
)
def test_add(a: Union[int, float], b: Union[int, float], expected: Union[int, float]):
    result = add(a, b) 
    
    assert result == expected
