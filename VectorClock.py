# Fill in your start vector values
vectors = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Fill in
# message = from to , event(increment) = x
# Example: task_list = [["13", "2"], ["32"], ["21", "3"], ["31"]]
task_list = [[""]]  # Fill in
print(f"t0 {vectors}")


def update_vectors(vector_from, vector_to):
    updated_vector = vector_to
    for i, (f, t) in enumerate(zip(vector_from, vector_to)):
        if f > t:
            updated_vector[i] = f
    return updated_vector


for i, tasks in enumerate(task_list):
    for task in tasks:
        if len(task) == 2:
            f, t = int(task[0]) - 1, int(task[1]) - 1
            vectors[f][f] += 1
            vectors[t] = update_vectors(vectors[f], vectors[t])
            vectors[t][t] += 1
        else:
            inc = int(task[0])
            vectors[inc - 1][inc - 1] += 1
    print(f"t{i + 1} {vectors}")
