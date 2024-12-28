# imports 
import time 
import numpy as np 

from abc import ABC, abstractmethod
from typing import List 

# class definition
class Sort(ABC):
    """
    Abstract base class for sorting algorithms.
    Provides benchmarking and array management functionality.
    """
    
    def __init__(self, array: List[int]) -> None:
        """
        Initialize the Sort class with an array to be sorted.
        
        Args:
            array (List[int]): Input array to be sorted
        """
        self.array = array.copy()  # Create a copy to preserve original array
        self.execution_time = 0.0  # Store execution time
        self.array_size = len(array)
    
    @abstractmethod
    def sort(self) -> List[int]:
        """
        Abstract method to be implemented by child classes with specific sorting logic.
        
        Returns:
            List[int]: Sorted array
        """
        pass
    
    def benchmark(self) -> dict:
        """
        Benchmark the sorting algorithm and return execution statistics.
        
        Returns:
            dict: Dictionary containing benchmark results
        """
        start_time = time.perf_counter()
        sorted_array = self.sort()
        end_time = time.perf_counter()
        
        self.execution_time = end_time - start_time
        
        return {
            'algorithm': self.__class__.__name__,
            'array_size': self.array_size,
            'execution_time': self.execution_time,
            'sorted_array': sorted_array
        }
    
    def get_execution_time(self) -> float:
        """
        Get the last recorded execution time.
        
        Returns:
            float: Execution time in seconds
        """
        return self.execution_time

    def __str__(self) -> str:
        return f"{self.__class__.__name__} : {self.p}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} : {self.p}"
    
    def __len__(self) -> int:
        return self.n