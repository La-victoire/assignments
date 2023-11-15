# Assignment Question:  Calculate the sum of all items in data using python3
# loops.

data: list[list[int]] = [
    [13, 15, 16],
    [12, 29, 50],
    [15, 23, 24],
]


index_sum = 0
value_sum = 0

# Access by index
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        index_sum += data[i][j]

print(f"The value of sum using index is {index_sum}")


# Access by value
for item in data:
    for n in item:
        value_sum += n

print(f"The value of sum using value is {value_sum}")


# Access by enumerate
for i, v in enumerate(data):
    print(f"Index is {i} and value is {v}")

# This is what enumerate function will return based on the argument we passed
# into it. It returns a lists of index and value pairs. This is the return list
# under the hood.
# [
#     [0, [13, 15, 16]],
#     [1, [12, 29, 50]],
#     [2, [15, 23, 24]],
# ]
