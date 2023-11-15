# Assignment Question:  Calculate the sum of all items in data using python3
# loops.

data: list[list[int]] = [
    [13, 15, 16],
    [12, 29, 50],
    [15, 23, 24],
]

sum = 0

# Your code goes here.
for i in range(0 ,len(data)):


    for j in range(0 , len(data[i])):
        sum+=data[i][j]

    print(f"The value of sum is {sum}")
