ka_pu = int(input("Public Key A: "))
ka_pr = int(input("Private Key A: "))
na = int(input("N modules A: "))
kb_pu = int(input("Public Key B: "))
kb_pr = int(input("Private Key B: "))
nb = int(input("N modules B: "))
message = int(input("Message: "))
h = int(input("Hash function value: "))


def E(K, m, n):
    return (m ** K) % n


def H(m):
    return m % h


print(f"Confidentiality: {E(kb_pu, message, nb)}")
print(f"Authenticity and Integrity: {E(ka_pr, H(message), na)}")
