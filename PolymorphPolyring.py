class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.parent = None
        self.children = []


def construct_graph(depth, node_amount):
    graph = [Node(str(i)) for i in range(node_amount)]

    for d in range(1, depth):
        next_layer = []
        for node in graph:
            for i in range(node_amount):
                child_identifier = node.identifier + '.' + str(i)
                child = Node(child_identifier)
                child.parent = node
                node.children.append(child)
                next_layer.append(child)
        graph = next_layer

    return graph


def print_graph(node, depth=0):
    parent_identifiers = ' ; '.join([ancestor.identifier for ancestor in get_ancestors(node)])
    print('  ' * depth + f"{node.identifier} (Ancestors: {parent_identifiers})")
    for child in node.children:
        print_graph(child, depth + 1)


def get_ancestors(node):
    ancestors = []
    current_node = node.parent
    while current_node:
        ancestors.append(current_node)
        current_node = current_node.parent
    return ancestors[::-1]


def calculate_matching_coordinates(guid1, guid2):
    # Split the GUIDs into lists of coordinates
    coords1 = guid1.split('.')
    coords2 = guid2.split('.')

    matching_coords = 0
    for coord1, coord2 in zip(coords1, coords2):
        if coord1 == coord2:
            matching_coords += 1
        else:
            break
    return matching_coords


def get_first_node(node):
    current_node = node
    while current_node.parent:
        current_node = current_node.parent
    return current_node


def find_node_by_prefix(graph, prefix):
    for node in graph:
        if node.identifier.startswith(prefix):
            current_node = node
            while current_node.identifier != prefix:
                current_node = current_node.parent
            return current_node
    return None


def find_path_in_polyring(start_node, end_node):
    path = [start_node.identifier]
    sibling_count = 0

    while start_node.identifier != end_node.identifier:
        # LR = Length of Routing
        length_of_routing = len(start_node.identifier.split('.'))
        # LD = Length of Destination
        length_of_destination = len(end_node.identifier.split('.'))
        # Number of Matching coordinates between routing peer's GUID and destination peer's GUID
        matching_coords = calculate_matching_coordinates(start_node.identifier, end_node.identifier)

        if matching_coords <= length_of_routing - 2:
            # Not same parent. Route to parent.
            start_node = start_node.parent
            path.append(start_node.identifier)
            sibling_count = 0

        elif matching_coords == length_of_routing - 1:
            if length_of_destination == length_of_routing - 1:
                # Destination is parent. Route to parent.
                start_node = start_node.parent
                path.append(start_node.identifier)
                sibling_count = 0
            elif length_of_destination >= length_of_routing:
                # Destination is sibling or sibling descendant. Route to sibling.
                start_node = start_node.parent
                if start_node is None:
                    start_node = get_first_node(end_node)
                else:
                    start_node = start_node.children[sibling_count]
                    sibling_count += 1
                if not start_node.identifier in path:
                    path.append(start_node.identifier)
        elif matching_coords == length_of_routing:
            sibling_count = 0
            if length_of_routing < length_of_destination:
                # Destination is descendant. Route to child.
                start_node = start_node.children[sibling_count]
            path.append(start_node.identifier)
    return path


if __name__ == '__main__':
    depth = int(input("Depth: "))
    node_amount = int(input("Node Amounts per Depth: "))
    graph = construct_graph(depth, node_amount)

    start_guid = input("Start Node Identifier: ")
    end_guid = input("End Node Identifier: ")

    start_node = find_node_by_prefix(graph, start_guid)
    end_node = find_node_by_prefix(graph, end_guid)

    if start_node is None:
        print(f"No node found with prefix '{start_guid}'")
    elif end_node is None:
        print(f"No node found with prefix '{end_guid}'")
    else:
        path = find_path_in_polyring(start_node, end_node)
        if path:
            print("Path found:")
            print(" -> ".join(path))
        else:
            print("No path found.")
