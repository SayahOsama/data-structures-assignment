def ticket_counter_simulation(customers):
    served_customers = []
    while customers:
        served_customers.append(customers.pop(0))
    return served_customers

print(ticket_counter_simulation(["Alice", "Bob", "Charlie"]))  # Output: ["Alice", "Bob", "Charlie"]
print(ticket_counter_simulation(["John", "Doe"]))  # Output: ["John", "Doe"]
print(ticket_counter_simulation([]))  # Output: []
print(ticket_counter_simulation(["OnlyOne"]))  # Output: ["OnlyOne"]