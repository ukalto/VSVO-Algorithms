processors = int(input("Amount of processor: "))
rows = int(input("Amount of rows: "))
# message from[1-Processor], to[1-Processor], step from [1-rows]
# Example: messages = [[1, 2, 2], [2, 3, 4], [3, 2, 7], [2, 1, 9]]
messages = [[]]  # Fill in
number_sequences = []
vectors = {}
for i in range(processors):
    number_sequences.append(int(input(f"Sequence number {i + 1}: ")))
    vectors[i + 1] = []
    for j in range(rows):
        vectors[i + 1].append(j * number_sequences[i])

for message in messages:
    f, t, step = message
    if vectors.get(f)[step - 1] > vectors.get(t)[step - 1]:
        vectors.get(t)[step] = vectors.get(f)[step - 1] + 1
        for x in range(step + 1, rows):
            vectors.get(t)[x] = vectors.get(t)[x - 1] + number_sequences[t - 1]

[print(f"{z}") for z in vectors.items()]
