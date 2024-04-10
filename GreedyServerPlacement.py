# Each Array is one L column
# Example: options = [[1, 10, 10], [10, 5, 3], [10, 6, 5]]
options = [[]] # Fill in
first_server = list(min({i + 1: sum(x) for i, x in enumerate(options)}.items(), key=lambda x: x[1]))
minimum = {}
for i, option in enumerate(options):
    temp = 0
    curr = []
    if i != first_server[0] - 1:
        for j, o in enumerate(option):
            curr.append(o if o < options[first_server[0] - 1][j] else options[first_server[0] - 1][j])
        minimum[i + 1] = curr

second_server = list(min({key: sum(value) for key, value in minimum.items()}.items(), key=lambda x: x[1]))

print(f"First Server to select: L{first_server[0]}")
print(f"Second Server to select: L{second_server[0]}")
print(f"Total Latency of the solution: {second_server[1]}")
