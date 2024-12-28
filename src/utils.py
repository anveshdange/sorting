"""
Author: Anvesh Dange
Date Created: 28-12-2024
Last Modified: 28-12-2024
Description:
    This file contains all the utilities required to benchmark and use the sorting algorithms

Usage:
    NotImplementedError

License: MIT 
"""

import numpy as np
from typing import List

def generate_random_array(size: int) -> List[int]:
    """
    Generate a random array of integers between 1 and 500.
    
    Args:
        size (int): The size of the array to generate
        
    Returns:
        List[int]: Array of random integers
        
    Raises:
        ValueError: If size is not an integer or is less than 1
    """
    # Check if the input is actually an integer
    if not isinstance(size, int):
        raise ValueError("Input must be an integer")
    
    # Check if the size is valid
    if size < 1:
        raise ValueError("Array size must be at least 1")
    
    # Generate random array using numpy
    random_array = np.random.randint(low=1, high=501, size=size)
    
    # Convert to regular Python list before returning
    return random_array.tolist()

