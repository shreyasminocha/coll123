import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from secret import flag

key = RSA.generate(1024)
cipher = PKCS1_OAEP.new(key)  # based (on RSA)

print(f"n = {key.n}")
print(f"e = {key.e}")

ciphertext = cipher.encrypt(flag)

print(f"ciphertext = {ciphertext.hex()}")

print()
print(key.export_key().decode())
print()
