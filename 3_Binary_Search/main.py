import time
import random
import matplotlib.pyplot as plt

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def analyze_binary_search(sizes):
    results = {'best': [], 'average': [], 'worst': []}
    for size in sizes:
        arr = sorted([random.randint(0, size*2) for _ in range(size)])
        
        # Best case: element is in the middle
        best_case_element = arr[size//2]
        start_time = time.time()
        binary_search_iterative(arr, best_case_element)
        end_time = time.time()
        results['best'].append(end_time - start_time)

        # Average case: element is random
        avg_case_element = random.randint(0, size*2)
        start_time = time.time()
        binary_search_iterative(arr, avg_case_element)
        end_time = time.time()
        results['average'].append(end_time - start_time)

        # Worst case: element is not in the array
        worst_case_element = -1 
        start_time = time.time()
        binary_search_iterative(arr, worst_case_element)
        end_time = time.time()
        results['worst'].append(end_time - start_time)
        
    return results

if __name__ == '__main__':
    input_sizes = [100, 500, 1000, 5000, 10000]
    analysis_results = analyze_binary_search(input_sizes)

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, analysis_results['best'], marker='o', label='Best Case')
    plt.plot(input_sizes, analysis_results['average'], marker='o', label='Average Case')
    plt.plot(input_sizes, analysis_results['worst'], marker='o', label='Worst Case')
    
    plt.title('Binary Search Complexity Analysis')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig('3_Binary_Search/binary_search_analysis.png')
    plt.show()
