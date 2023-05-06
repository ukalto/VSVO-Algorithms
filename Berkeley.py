from datetime import timedelta

# Input-format example: for 3:30 pm = 1530
server_a_time = input("Server A: ")
server_b_time = input("Server B: ")
server_c_time = input("Server C: ")


def convert_seconds(time):
    m, s = divmod(abs(time), 60)
    h, m = divmod(m, 60)
    sign = " "
    if time < 0:
        sign = "-"
    return f"{sign}{int(h)}:{int(m)}:{int(s)}"


server_a = ["Server A", timedelta(hours=int(server_a_time[:len(server_a_time) // 2]), minutes=int(server_a_time[len(server_a_time) // 2:])).total_seconds()]
server_b = ["Server B", timedelta(hours=int(server_b_time[:len(server_b_time) // 2]), minutes=int(server_b_time[len(server_b_time) // 2:])).total_seconds()]
server_c = ["Server C", timedelta(hours=int(server_c_time[:len(server_c_time) // 2]), minutes=int(server_c_time[len(server_c_time) // 2:])).total_seconds()]
servers = [server_a, server_b, server_c]
# Scenario: rounds = 3 | Time Demon = Server A
print("\nRound 1")
print(f"Server A to {server_a[0]}: {convert_seconds(server_a[1])}")
print(f"Server A to {server_b[0]}: {convert_seconds(server_a[1])}")
print(f"Server A to {server_c[0]}: {convert_seconds(server_a[1])}")

print("\nRound 2")
diff_a = server_a[1] - server_a[1]
diff_b = server_b[1] - server_a[1]
diff_c = server_c[1] - server_a[1]
print(f"{server_a[0]} to Server A: {convert_seconds(diff_a)}")
print(f"{server_b[0]} to Server A: {convert_seconds(diff_b)}")
print(f"{server_c[0]} to Server A: {convert_seconds(diff_c)}")

print("\nRound 3")
avg = (diff_a + diff_b + diff_c) / 3
new_a = server_a[1] + avg
diff_b = new_a - server_b[1]
diff_c = new_a - server_c[1]
print(f"Server A to {server_a[0]}: {convert_seconds(avg)}")
print(f"Server A to {server_b[0]}: {convert_seconds(diff_b)}")
print(f"Server A to {server_c[0]}: {convert_seconds(diff_c)}")
