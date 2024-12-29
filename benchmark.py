# imports
import os
import numpy as np
import matplotlib.pyplot as plt
import argparse

# module imports
from src.utils import generate_random_array
from src.algorithms.bubble import BubbleSort
from src.algorithms.selection import SelectionSort
from typing import List, Iterable # for type hinting

def run_benchmark(args):
    """
    Run performance benchmarks for sorting algorithms and create visualization.
    This function executes benchmarks for specified sorting algorithms (bubble sort and/or
    selection sort) across different array sizes and generates a plot comparing their
    performance.
    Args:
        args: Namespace object containing the following attributes:

            -- start (int): Starting array size for benchmarking
            -- end (int): Ending array size for benchmarking
            -- step (int): Step size between array sizes
            -- algorithms (list): List of algorithms to benchmark ('bubble' and/or 'selection')
            -- figsize (int): Size of the output plot figure
            -- title (str): Title for the plot
            -- output (str): Output directory path for saving the plot
            -- show (bool): Whether to display the plot interactively
            -- sorted(bool): Whether to use presorted arrays for benchmarking
    Returns:
        None
    """
    # Create array sizes to test
    array_sizes: Iterable[int] = range(args.start, args.end + 1, args.step)
    
    # Lists to store execution times
    times = {
        'bubble': [] if 'bubble' in args.algorithms else None,
        'selection': [] if 'selection' in args.algorithms else None
    }
    
    if args.sorted: print("\033[92mNOTE: Using presorted array for benchmarking\033[0m") 
    
    # Benchmark algorithms
    for size in array_sizes:
        array: List[int] = generate_random_array(size)
        
        if args.sorted:
            array.sort()
            
        if 'bubble' in args.algorithms:
            bubble = BubbleSort(array.copy())
            times['bubble'].append(bubble.benchmark()['execution_time'])
            
        if 'selection' in args.algorithms:
            selection = SelectionSort(array.copy())
            times['selection'].append(selection.benchmark()['execution_time'])
    
    # Create plot
    plt.figure(figsize=(args.figsize, args.figsize * 0.6))
    
    if times['bubble']:
        plt.plot(array_sizes, times['bubble'], 'b-o', label='Bubble Sort')
    if times['selection']:
        plt.plot(array_sizes, times['selection'], 'r-o', label='Selection Sort')
    # Customize plot appearance
    plt.title(args.title)
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.legend()
    
    if not os.path.exists(args.output): 
        os.makedirs(args.output, exist_ok=True)
    
    # Create output directory if it doesn't exist
    if args.sorted:
        if not os.path.exists(os.path.join(args.output, 'sorted')):
            sorted_path: str = os.path.join(args.output, 'sorted')
            os.makedirs(sorted_path, exist_ok=True)

        
    
    # Save plot to file if sorted array is used
    if args.sorted:
        sorted_path: str = os.path.join(args.output, 'sorted')
        plt.savefig(os.path.join(sorted_path, f'benchmark_{args.start}_{args.end}_sorted.png'))

    # Save the plot to file if not using sorted array
    plt.savefig(os.path.join(args.output, f'benchmark_{args.start}_{args.end}.png'))
    
    # Show plot if requested
    if args.show:
        plt.show()

# main function to call the benchmark function
def main():
    
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Benchmark sorting algorithms')

    # Add arguments with default values
    parser.add_argument('--start', type=int, default=500, help='Starting array size')
    parser.add_argument('--end', type=int, default=10000, help='Ending array size')
    parser.add_argument('--step', type=int, default=500, help='Step size for array sizes')
    parser.add_argument('--output', type=str, default='figures', help='Output directory')
    parser.add_argument('--algorithms', nargs='+', default=['bubble', 'selection'],
                        choices=['bubble', 'selection'], help='Algorithms to benchmark')
    parser.add_argument('--figsize', type=int, default=10, help='Figure size')
    parser.add_argument('--title', type=str, default='Sorting Algorithm Performance Comparison',
                        help='Plot title')
    parser.add_argument('--show', action='store_true', help='Display plot')
    parser.add_argument('--sorted', action='store_true', default=False, help='Use presorted arrays')

    # Parse command line arguments
    args = parser.parse_args()
    # Run the benchmark with parsed arguments
    run_benchmark(args)

# driver code
if __name__ == '__main__':
    main()