def update_vectors(vector_from, vector_to):
    updated_vector = vector_to
    for idx, (v_from, v_to) in enumerate(zip(vector_from, vector_to)):
        if v_from > v_to:
            updated_vector[idx] = v_from
    return updated_vector


def solve_vector_clocks(task_list):
    for i, tasks in enumerate(task_list):
        for task in tasks:
            if len(task) == 2:
                v_from, v_to = int(task[0]) - 1, int(task[1]) - 1
                vectors[v_from][v_from] += 1
                vectors[v_to] = update_vectors(vectors[v_from], vectors[v_to])
                vectors[v_to][v_to] += 1
            else:
                inc = int(task[0])
                vectors[inc - 1][inc - 1] += 1
        print(f"t{i + 1} {vectors}")


if __name__ == '__main__':
    # Fill in your start vector values
    vectors = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Fill in
    # message = from to , event(increment) = x
    # Example: task_list = [["13", "2"], ["32"], ["21", "3"], ["31"]]
    task_list = [[]]  # Fill in
    print(f"t0 {vectors}")

    solve_vector_clocks(task_list)
