def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):  # Subdirectory
            total_size += calculate_directory_size(value)
        else:  # File
            total_size += value
    return total_size

# Example Directory Tree
directory_tree = {
    "Root": {
        "Sub1": 5,
        "Sub2": {
            "File3": 15
        },
        "File1": 10,
        "File2": 5
    }
}

# Initial Calculation
print(calculate_directory_size(directory_tree["Root"]))  # Output: 35

# Add a File under Sub2
directory_tree["Root"]["Sub2"]["File4"] = 20
print(calculate_directory_size(directory_tree["Root"]))  # Output: 55

# Remove File1
del directory_tree["Root"]["File1"]
print(calculate_directory_size(directory_tree["Root"]))  # Output: 45
