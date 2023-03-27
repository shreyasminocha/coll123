import os
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from secret import flag


def debug(s):
    if not os.environ.get("PROD"):
        print(s)


p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)

e = 65537
d = pow(e, -1, phi)

m = bytes_to_long(flag)

assert m < n

c = pow(m, e, n)
ciphertext = long_to_bytes(c)

print(f"n = {n}")
print(f"e = {e}")
debug(f"d = {d}")
print(f"ciphertext = {ciphertext.hex()}")
