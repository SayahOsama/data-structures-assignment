def undo_operation(operations):
    if len(operations) == 0:
        return operations
    operations.pop()
    return operations

operations = ["type A","type B","delete"]
print("Input: ",operations, "Output: ",undo_operation(operations))