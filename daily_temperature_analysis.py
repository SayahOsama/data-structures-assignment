
def temperature_analysis(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for current_day, current_temp in enumerate(temperatures):
        
        while stack and temperatures[stack[-1]] < current_temp:
            previous_day = stack.pop()
            result[previous_day] = current_day - previous_day
            
        stack.append(current_day)
    
    return result
        
# Examples
print(temperature_analysis([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
print(temperature_analysis([30, 40, 50, 60]))  # Output: [1, 1, 1, 0]
print(temperature_analysis([60, 50, 40]))  # Output: [0, 0, 0]
print(temperature_analysis([30]))  # Output: [0]