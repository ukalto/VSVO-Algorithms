from datetime import timedelta


class Server:
    def __init__(self, name, time):
        self.name = name
        self.time = timedelta(hours=int(time[:len(time) // 2]), minutes=int(time[len(time) // 2:])).total_seconds()
        self.time_daemon = False


def start_app():
    servers = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # Input-format example: for 3:30 pm = 1530
    for i in range(int(input("How many servers? "))):
        s = input(f"Server {letters[i]}: ")
        servers.append(Server(f"Server {letters[i]}", s))
    while True:
        print(f"\nWhich server is the time daemon? Range: 0-{len(servers) - 1}")
        time_daemon = int(input("Time Daemon: "))
        if time_daemon < 0 or time_daemon > len(servers):
            print("Invalid input")
        else:
            servers[time_daemon].time_daemon = True
            break
    return servers, servers[time_daemon]


def convert_seconds(time):
    m, s = divmod(abs(time), 60)
    h, m = divmod(m, 60)
    sign = " "
    if time < 0:
        sign = "-"
    return f"{sign}{int(h):02d}:{int(m):02d}:{int(s):02d}"


def round_one(servers, time_daemon):
    print("\nRound 1")
    for s in servers:
        print(f"{time_daemon.name} {s.name}: {convert_seconds(s.time)}")


def round_two(servers, time_daemon):
    print("\nRound 2")
    differences = []
    for s in servers:
        diff = s.time - time_daemon.time
        print(f"{s.name} to {time_daemon.name}: {convert_seconds(diff)}")
        differences.append(diff)
    return differences


def round_three(servers, time_differences, time_daemon):
    print("\nRound 3")
    avg = sum(time_differences) / len(time_differences)
    for s in servers:
        diff = time_daemon.time + avg - s.time
        print(f"{time_daemon.name} to {s.name}: {convert_seconds(diff)} | Final Time: {convert_seconds(s.time + diff)}")


if __name__ == '__main__':
    network_servers, time_daemon = start_app()

    round_one(network_servers, time_daemon)

    time_differences = round_two(network_servers, time_daemon)

    round_three(network_servers, time_differences, time_daemon)
