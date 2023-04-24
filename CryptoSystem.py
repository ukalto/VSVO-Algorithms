ka_pu = int(input("Public Key A: "))
ka_pr = int(input("Private Key A: "))
na = int(input("N modules A: "))
kb_pu = int(input("Public Key B: "))
kb_pr = int(input("Private Key B: "))
nb = int(input("N modules B: "))
message = int(input("Message: "))
h = int(input("Hash function value: "))
confidentiality = True if input("Confidentiality y:") == "y" else False
authenticity = True if input("Authenticity y: ") == "y" else False
integrity = True if input("Integrity y: ") == "y" else False


def E(K, m, n):
    return (m ** K) % n


def H(m):
    return m % h


# From A - B
if confidentiality and not authenticity and not integrity:
    print(E(kb_pu, message, nb))
elif not confidentiality and authenticity and not integrity:
    print(E(ka_pr, message, na))
elif not confidentiality and not authenticity and integrity:
    print(H(message))
elif not confidentiality and authenticity and integrity:
    print(E(ka_pr, H(message), na))
else:
    print("no possible option at this time")
