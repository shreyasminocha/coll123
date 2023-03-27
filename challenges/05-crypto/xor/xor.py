import os
import sys
import random
import secrets
from secret import flag

plaintext = random.randbytes(20)
key = secrets.token_bytes(len(plaintext))
ciphertext = [c ^ k for c, k in zip(plaintext, key)]

print("key (hex) =", key.hex())
print("ciphertext (hex) =", bytes(ciphertext).hex())

try:
    guess = bytes.fromhex(input("plaintext (hex) = ").strip())
except ValueError:
    print("that's not valid hex :(")
    exit()

if guess == plaintext:
    sys.stdout.buffer.write(flag)
    print()
else:
    print("that's not correct :(")
