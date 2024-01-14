# Input parsing
nodes_length = int(input("How many nodes exist?: "))
bit_id = int(input("Bit-Identifier?: "))
start_node = ""
key = ""
path = []

try:
    start_node = int(input("Start-Node: "))
    key = int(input("Key: "))
    path.append(start_node)
except ValueError:
    pass

entities = []
entities_dict = {}

while True:
    try:
        node = int(input("Black Dots: "))
        entities.append(node)
        entities_dict[node] = ""
    except ValueError:
        break


# finds successor of given node
def find_succ(node):
    above = [i for i in entities if node <= i]
    return min(above) if above != [] else entities[0]


def find_closest(list):
    # ID, shortest-distance
    curr = []
    for i in range(len(list)):
        dist = (nodes_length - list[i] + key) % nodes_length
        if not curr or curr[1] > dist:
            curr = [list[i], dist]
    return curr


for node in entities:
    nodes = []
    for i in range(1, bit_id + 1):
        nodes.append(find_succ((node + pow(2, i - 1)) % nodes_length))
    entities_dict[node] = nodes

if key and start_node:
    closest = []
    for i in range(len(entities_dict)):
        try:
            temp = find_closest(entities_dict.get(path[i]))
            if not closest or closest[1] > temp[1]:
                closest = temp
                path.append(closest[0])
        except IndexError:
            path.append(entities_dict.get(path[-1])[0])
            print(path)
            break
else:
    # prints the list
    for key, entries in entities_dict.items():
        print(f"\nNode: {key}")
        [print(f"ID: {i + 1} Node: {entry}") for i, entry in enumerate(entries)]
