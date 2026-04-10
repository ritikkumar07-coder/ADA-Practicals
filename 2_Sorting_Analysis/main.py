import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def analyze_sorting(sort_function, case, sizes):
    times = []
    for size in sizes:
        if case == 'best':
            arr = list(range(size))
        elif case == 'worst':
            arr = list(range(size, 0, -1))
        else: # average
            arr = [random.randint(0, 1000) for _ in range(size)]
        
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

if __name__ == '__main__':
    sizes = [10, 20, 30, 40]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort
    }
    cases = ['best', 'average', 'worst']
    
    results = {}

    for name, func in algorithms.items():
        results[name] = {}
        for case in cases:
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
        plt.savefig(f'2_Sorting_Analysis/{case}_case_analysis.png')
        plt.show()
