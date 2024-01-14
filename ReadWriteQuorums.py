import random

N = int(input("N: "))
try: read_important = int(input("1 = True : Other = False ")) == 1
except ValueError: read_important = False

if read_important:
    print(f"N_r = {1}\nN_w = {N}")
else:
    x = random.randint(N // 2, N)
    y = random.randint(N - x + 1, N)
    print(f"N_r = {y}\nN_w = {x}")
