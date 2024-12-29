# Filename: sorting.py

#imports 
import numpy as np 
from typing import List 
from utils import generate_random_array

# set the global random seed 
np.random.seed(42) 

# code for bubble sort
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

# code for selection sort
def insertion_sort(p:List[int]) -> List[int]:  pass


# code for insertion sort
def selection_sort(p:List[int]) -> List[int]:
    """ 
    Function to sort the array using bubble sort algorithm.

    Args: 
    p: List[int] : input array to be sorted 

    Returns: 
        sorted array of integers 
    """
    length:int = len(p)
    for i in range(length): 
        min_index: int = i 
        for j in range(i, length): 
            if p[j] < p[min_index]: 
                min_index=j 
        if min_index != i: 
            p[i], p[min_index] = p[min_index], p[i]
    return p


# Driver code 
if __name__ == "__main__" : 
  dummy_array: List[int] = generate_random_array(5)
  print(f"Dummy array: {dummy_array}") 

  sorted_bubble: List[int] = bubble_sort(dummy_array) 
  sorted_selection: List[int] = selection_sort(dummy_array)

  print(f"Bubble: {sorted_bubble}")
  print(f"Selection: {sorted_selection}")