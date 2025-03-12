from tabulate import tabulate

options = []
num_clients = int(input("Enter the number of clients: "))
num_latencies = int(input("Enter the number of latencies per client: "))

for i in range(num_clients):
    latencies = []
    for j in range(num_latencies):
        latency = int(input(f"Enter latency for client {i + 1}, latency {j + 1}: "))
        latencies.append(latency)
    options.append(latencies)

# Create headers
headers = [""] + [f"L{j + 1}" for j in range(num_latencies)]
table = [[f"C{i + 1}"] + options[i] for i in range(num_clients)]

# Print the table
print(tabulate(table, headers, tablefmt="grid"))

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