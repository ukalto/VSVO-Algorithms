def print_hline(l_col_width, col_widths, location_num):
    out = "\n" + "-" * (l_col_width)
    for i in range(0, location_num):
        out += "+" + "-" * col_widths[i]
    print(out)

location_num = int(input("Number of Locations: "))
client_num = int(input("Number of clients: "))
placement_num = int(input("How many servers to place: "))

options = [[0] * client_num for i in range(location_num)]
CLIENT_PREFIX = "Client"
LOCATION_PREFIX = "L"
L_COL_LEN = len(CLIENT_PREFIX) + 1 + len(str(client_num)) + 1  # Length of the left most column

# Separator
print()

for i in range(1, client_num+1):
    for j in range(1, location_num+1):
        options[j-1][i-1] = int(input(f"Client {i} latency {j}: "))

# Separator
print()

col_widths = [0] * location_num
for i in range(0, location_num):
    col_widths[i] = max(len(str(max(options[i]))), len(LOCATION_PREFIX + str(location_num))) + 2
    # Make the column size even to have it nicely centered
    if col_widths[i] % 2 == 1:
        col_widths[i] += 1

# Print header for table
print(" " * L_COL_LEN, end="")  # Reserve enough space for the leftmost column
for i in range(0, location_num):
    print("|" + f"L{i+1}".center(col_widths[i], " "), end="")

print_hline(L_COL_LEN, col_widths, location_num)

# Print table
for i in range(1, client_num+1):
    print(f"{CLIENT_PREFIX} {i}".ljust(L_COL_LEN), end="")
    for j in range(1, location_num+1):
        print("| " + str(options[j-1][i-1]).ljust(col_widths[j-1]-1), end="")
    print()

# Separator
print()

# Select the server with the lowest latency for all clients
selected_servers = [False] * len(options)
minimum_index = 0
minimum = sum(options[minimum_index])
for i in range(1, len(options)):
    latency = sum(options[i])
    if latency < minimum:
        minimum = latency
        minimum_index = i

print(f"\nServer 1 placement: L{minimum_index+1}")
selected_servers[minimum_index] = True

for n in range(2, placement_num+1):
    minimum_index = None
    minimum = None
    for candidate in range(len(options)):
        # Skip if we already have placed a server in this location
        if selected_servers[candidate]:
            continue

        # Find the minimum latency for all clients from the candidate and all selected locations
        latency = [0] * client_num
        for i in range(client_num):
            latency[i] = options[candidate][i]
            for j in range(len(options)):
                # Skip all servers not selected
                if selected_servers[j]:
                    if options[j][i] < latency[i]:
                        latency[i] = options[j][i]

        latency_sum = sum(latency)
        if minimum is None or latency_sum < minimum:
            minimum = latency_sum
            minimum_index = candidate

    print(f"Server {n} placement: L{minimum_index+1}")
    selected_servers[minimum_index] = True

print(f"Total latency of the solution: {minimum}")
