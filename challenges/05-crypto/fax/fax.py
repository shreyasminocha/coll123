from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from secret import flag

p = getPrime(1 << (12 >> 1))
q = getPrime(1 << (12 >> 1))
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
print(f"ciphertext = {ciphertext.hex()}")
