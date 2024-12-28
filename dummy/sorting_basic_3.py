# below code is for setting the path for the module utils to load generate_random_array function
# not really know what below three lines are doing 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# imports 
import numpy as np
from typing import List 
from src.utils import generate_random_array 

# Set the global random seed
np.random.seed(42)

def bubble_sort(p:List[int]) -> List[int] :
    """ 
    Function to sort the array using bubble sort algorithm.

    Args: 
    p: List[int] : input array to be sorted 

    Returns: 
        sorted array of integers 
    """
    
    n: int = len(p) 

    # traverse through all array elements 
    for i in range(n) : 
        swapped: bool = False 

        # Last i elements are already in place 
        for j in range(0, n-i-1) :
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater 
            # increment the pointer otherwise
            if p[j] > p[j+1] :
                p[j], p[j+1] = p[j+1], p[j]
                swapped = True 
        # when no element gets swapped the array is already sorted.
        if not swapped : break
    return p

def insertion_sort(p:List[int]) -> List[int]:
    """ 
    Function to sort the array using insertion sort algorithm.

    Args: 
    p: List[int] : input array to be sorted 

    Returns: 
        sorted array of integers 
    """ 
    raise NotImplementedError

def selection_sort(p:List[int]) -> List[int] : 
    """ 
    Function to sort the array using selection sort algorithm.

    Args: 
    p: List[int] : input array to be sorted 

    Returns: 
        sorted array of integers 
    """
    raise NotImplementedError

# driver code
if __name__ == "__main__" : 
    dummy_array: List[int] = generate_random_array(5) 
    print(dummy_array)

    # applying sorting using functions
    sorted_bubble: List[int] = bubble_sort(dummy_array) 
    sorted_selection: List[int] = selection_sort(dummy_array)
    sorted_insertion: List[int] = insertion_sort(dummy_array)
    

    # printing the results
    print(sorted_bubble) 
    print(sorted_selection)
    print(sorted_insertion)