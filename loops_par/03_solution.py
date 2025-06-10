number = 10
table_range = 10
for i in range(1, table_range + 1):
    if i == 5:
        continue
    print(number, "x", i, "=", number * i)
    