# imports 
from typing import List
from .sort import Sort 

class BubbleSort(Sort):
    """
    Implementation of Bubble Sort algorithm.
    Inherits from base Sort class.
    """
    
    def sort(self) -> List[int]:
        """
        Implementation of bubble sort algorithm.
        
        Returns:
            List[int]: Sorted array
        """
        arr = self.array.copy()  # Work with a copy of the array
        n = len(arr)
        
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr