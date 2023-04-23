nodes_length = int(input("How many nodes exist?: "))
bit_id = int(input("Bit identifier?: "))
entities = []
while True:
    try:
        entities.append(int(input("Black dotted: ")))
    except:
        break


def find_succ(node):
    above = [i for i in entities if node <= i]
    return min(above) if above != [] else entities[0]


for node in entities:
    message = ""
    for i in range(1, bit_id + 1):
        message += f"ID: {i} Node: {find_succ((node + pow(2, i - 1)) % nodes_length)}\n"
    print(message)
