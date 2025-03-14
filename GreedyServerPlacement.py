from tabulate import tabulate

num_latencies = int(input("Enter the number of latencies per client: "))
num_clients = int(input("Enter the number of clients: "))
options = [[0 for _ in range(num_latencies)] for _ in range(num_clients)]

for i in range(num_clients):
    for j in range(num_latencies):
        latency = int(input(f"Enter latency for client {i + 1}, latency {j + 1}: "))
        options[j][i] = latency

# Create headers
headers = [""] + [f"L{j + 1}" for j in range(num_latencies)]
table = [[f"C{i + 1}"] + [options[j][i] for j in range(num_latencies)] for i in range(num_clients)]
# Print the table
print(tabulate(table, headers, tablefmt="grid"))

# Calculate total latency for each server
total_latencies = {i + 1: sum(x) for i, x in enumerate(options)}

# Find the first server with the minimum total latency
first_server = min(total_latencies.items(), key=lambda x: x[1])

# Calculate the minimum latencies for the remaining servers
minimum = {}
for i, option in enumerate(options):
    if i != first_server[0] - 1:
        curr = [min(o, options[first_server[0] - 1][j]) for j, o in enumerate(option)]
        minimum[i + 1] = curr

# Find the second server with the minimum total latency
second_server = min(minimum.items(), key=lambda x: sum(x[1]))

# Print the selected servers and total latency
print(f"First Server to select: L{first_server[0]}")
print(f"Second Server to select: L{second_server[0]}")
print(f"Total Latency of the solution: {sum(second_server[1])}")

print("-------------------------")

# Print all servers in descending order of total latency
print("Servers selected in descending order of total latency:")
for server, latency in total_latencies.items():
    print(f"Server L{server}: Total Latency = {latency}")