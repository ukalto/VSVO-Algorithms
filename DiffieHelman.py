n = int(input("n: "))
g = int(input("g: "))
a = int(input("a: "))
b = int(input("b: "))

print(f"{g}^({a}*{b}) mod {n}: {pow(g, a * b) % n}")
