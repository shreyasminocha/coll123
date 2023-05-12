import random
import secrets
from itertools import cycle
from secret import flag

key = secrets.token_bytes(8)
ciphertext = bytes([c ^ k for c, k in zip(flag, cycle(key))])

print("ciphertext =", ciphertext.hex())
print("no key for this one >:)")
