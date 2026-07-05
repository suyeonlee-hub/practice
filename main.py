from typing import Union, Optional

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]: -> Optional[Union[int, float]]:
    try:
        return x + y
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    
    return result

if __name__ == "__main__":
    print(add(5, 3))        # Output: 8
    print(add(5.5, 2.3))    # Output: 7
    print(add(5, 2.3))      # Output: 7.3