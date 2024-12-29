
import numpy as np
import matplotlib.pyplot as plt

from src.utils import generate_random_array
from src.algorithms.bubble import BubbleSort
from src.algorithms.selection import SelectionSort

from typing import List
from typing import Iterable

# Create array sizes to test
array_sizes: Iterable[int] = range(500, 5001, 500)

# Lists to store execution times
bubble_times: List[float] = []
selection_times: List[float] = []

# Benchmark both algorithms for different array sizes
for size in array_sizes:
    # Create the array of random sizes 
    array: List[int] = generate_random_array(size)

    # Create instances of sorting classes
    bubble: BubbleSort = BubbleSort(array) 
    selection: SelectionSort = SelectionSort(array) 
    
    # Get execution times using benchmark method
    # merge_time: float = merge_sorter.benchmark(size)
    bubble_time: float = bubble.benchmark()['execution_time']
    selection_time: float = selection.benchmark()['execution_time']
    
    # Store the times
    bubble_times.append(bubble_time)
    selection_times.append(selection_time)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, 'b-o', label='Bubble Sort')
plt.plot(array_sizes, selection_times, 'r-o', label='Selection Sort')

# Customize the plot
plt.title('Sorting Algorithm Performance Comparison')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()