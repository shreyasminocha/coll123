from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes, random
from sympy.ntheory.residue_ntheory import primitive_root
from secret import flag

# in practice, of course, the prime must be larger and must be chosen more
# carefully
p = getPrime(160)
g = primitive_root(p)

print(f"p = {p}")
print(f"g = {g}")

alice_private = random.randrange(2, p - 1)

alice_public = pow(g, alice_private, p)
print(f"A = {alice_public}")

print()
print("You are Mallory, an adversary who can pretend to be Bob")
bob_public = int(input("Enter a value for Bob's public integer (B): "))
print()

assert 2 <= bob_public <= p - 1

shared_k = pow(bob_public, alice_private, p)

BLOCK_SIZE = 16

salt = get_random_bytes(BLOCK_SIZE)
print(f"salt = {salt.hex()}")

# a key derivation function to generate a key from our shared secret
key = PBKDF2(long_to_bytes(shared_k), salt, BLOCK_SIZE)

iv = get_random_bytes(BLOCK_SIZE)
aes = AES.new(key, AES.MODE_CBC, iv)
ciphertext = aes.encrypt(pad(flag, BLOCK_SIZE))

print(f"iv = {iv.hex()}")
print(f"flag = {ciphertext.hex()}")
