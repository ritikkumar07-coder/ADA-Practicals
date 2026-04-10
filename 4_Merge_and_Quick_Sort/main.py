import time
import random
import sys
import matplotlib.pyplot as plt

# It's a good practice to increase the recursion limit for sorting large arrays
sys.setrecursionlimit(2000)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort_recursive(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi-1)
        quick_sort_recursive(arr, pi+1, high)

def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr)-1)


def analyze_sorting(sort_function, case, sizes):
    times = []
    for size in sizes:
        if case == 'best':
            # Best case for Quick Sort is a balanced partition, often with random data.
            # Best case for Merge Sort is not significantly different from average.
            arr = [random.randint(0, 1000) for _ in range(size)]
        elif case == 'worst':
            # Worst case for this Quick Sort implementation is a sorted or reverse-sorted array
            arr = list(range(size)) if sort_function == quick_sort else list(range(size, 0, -1))
        else: # average
            arr = [random.randint(0, 1000) for _ in range(size)]
        
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

if __name__ == '__main__':
    sizes = [100, 200, 500, 1000]
    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    cases = ['best', 'average', 'worst']
    
    results = {}

    for name, func in algorithms.items():
        results[name] = {}
        for case in cases:
            # For quick sort, we need to handle the recursion depth for the worst case
            if name == "Quick Sort" and case == 'worst':
                # Temporarily increase recursion limit for this specific case if needed
                # This is a simplified approach. A better quicksort uses random pivot.
                pass
            times = analyze_sorting(func, case, sizes)
            results[name][case] = times
            print(f"{name} - {case} case times: {times}")

    # Plotting
    for case in cases:
        plt.figure()
        plt.title(f'Sorting Algorithms Analysis ({case.capitalize()} Case)')
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time (s)')
        for name in algorithms.keys():
            plt.plot(sizes, results[name][case], marker='o', label=name)
        plt.legend()
        plt.grid(True)
        plt.savefig(f'4_Merge_and_Quick_Sort/{case}_case_analysis.png')
        plt.show()
