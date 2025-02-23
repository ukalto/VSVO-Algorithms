import platform

if platform.system() == 'Windows':
    try:
        import colorama
    except ImportError:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Enable ANSI support on Windows 10 v1511
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        colorama.init()

location_num = int(input("Number of Locations: "))
client_num = int(input("Number of clients: "))
placement_num = int(input("How many servers to place: "))

options = [[0] * client_num for i in range(location_num)]
CLIENT_PREFIX = "Client"
L_COL_LEN = (len(CLIENT_PREFIX)+3)  # Length of the left most column
COL_LEN = 6  # Length of all other columns

print("\nNow fill out the table:")

def print_hline():
    out = "\n" + "-" * (L_COL_LEN)
    for i in range(0, location_num):
        out += "+" + "-" * COL_LEN
    print(out)

def undo_newline(line_len):
    print(f"\033[{line_len}C\033[1A", end="")

# Print header for interactive table
print(" " * L_COL_LEN, end="")  # Reserve enough space for the leftmost column
for i in range(1, location_num+1):
    print("|" + f"L{i}".center(COL_LEN, " "), end="")

print_hline()

for i in range(1, client_num+1):
    print(f"{CLIENT_PREFIX} {i}".ljust(L_COL_LEN), end="")
    for j in range(1, location_num+1):
        options[j-1][i-1] = int(input("|"))
        undo_newline(L_COL_LEN + (1+COL_LEN)*j)
    #print_hline()
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
