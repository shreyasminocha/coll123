import os
import sys
import random
import secrets
from itertools import cycle
from secret import flag

key = cycle(secrets.token_bytes(1))

for _ in range(1000):
    plaintext = random.randbytes(20)
    ciphertext = [c ^ k for c, k in zip(plaintext, key)]
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
