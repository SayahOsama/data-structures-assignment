
def arrange_inventory_shelf(inventory):
    inventory.reverse()
    return inventory

book_IDs = [101,102,103,104]
print("reversed inventory: ", arrange_inventory_shelf(book_IDs))    