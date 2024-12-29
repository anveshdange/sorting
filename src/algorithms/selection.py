# imports 
from typing import List
from .sort import Sort 

class SelectionSort(Sort):
    """ 
    Implementation of Selection Sort Algorithm 
    Inherits from base Sort class.
    """
    
    def sort(self) -> List[int]: 
        """
        Implementation of selection sort algorithm
        
        Returns:
            List[int]: Sorted array
        """
        arr = self.array.copy()  # make a copy of the array provided 
        n = len(arr) 

        for i in range(n) : 
            min_index: int = i
            for j in range(i, n) :
                if arr[j] < arr[min_index] :
                    min_index = j
            if min_index != i :
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    