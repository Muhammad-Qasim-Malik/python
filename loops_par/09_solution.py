items = ["apple", "banana","banana", "orange", "apple", "mango"]
unique_items = set()
for i in items:
    if i in unique_items:
        print("Duplicate Item Found: (" + i + ")")
        break
    unique_items.add(i)