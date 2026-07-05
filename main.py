from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

if __name__ == "__main__":
    print(add(5, 3))        # Output: 8
    print(add(5.5, 2.3))    # Output: 7
    print(add(5, 2.3))      # Output: 7.3