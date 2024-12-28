
# imports
import numpy
from typing import List

from src.utils import generate_random_array 
from src.algorithms.bubble import BubbleSort

def test_random_array_generator(size: int) -> None: 
    """
    
    Tests the generate_random_array function from src.utils 

    Args: 
        size (int): The size of array to be generated 

    Returns: 
        Nothing, Prints the tests results passed or failed.
    
    Raises: 
        ValueError: If size is not an integer or is negative
    """
    numpy.random.seed(2007) # for reproducibility
    gen_array: List[int] = generate_random_array(size)
    assert len(gen_array) == size 
    print(gen_array) 
    return None 

def test_bubble_sort_class() -> None: 
    """
    
    Tests the Sort class from src/algorithms/sort.py 

    Args: 
        None 

    Returns: 
        Nothing, Prints the tests results passed or failed.
    
    Raises: 
        AssertionError: If the tests fail 
    """
    p: BubbleSort = BubbleSort([5, 4, 3, 2, 1]) 
    assert p.sort() == [1, 2, 3, 4, 5] 
    results: dict = p.benchmark()
    print(results)
    print(f"\nAlgorithm: {results['algorithm']}")
    print(f"Array size: {results['array_size']}")
    print(f"Execution time: {results['execution_time']:.6f} seconds")
    print("Sorted array:", results['sorted_array'])

##################################################
#                     DRIVER CODE 
##################################################
if __name__ == "__main__" : 
    test_random_array_generator(5)
    test_bubble_sort_class()