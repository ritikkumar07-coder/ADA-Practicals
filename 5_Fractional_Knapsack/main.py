def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0
    knapsack_vector = [0] * len(items)
    
    for i, (value, weight) in enumerate(items):
        if capacity == 0:
            break
        if weight <= capacity:
            # Take the whole item
            total_value += value
            knapsack_vector[i] = 1
            capacity -= weight
        else:
            # Take a fraction of the item
            fraction = capacity / weight
            total_value += value * fraction
            knapsack_vector[i] = fraction
            capacity = 0
            
    return total_value, knapsack_vector

if __name__ == '__main__':
    # (value, weight)
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    
    max_profit, vector = fractional_knapsack(items, capacity)
    
    print("Items (value, weight):", items)
    print("Knapsack capacity:", capacity)
    print("Maximum profit:", max_profit)
    print("Fraction of items taken (vector):", vector)
