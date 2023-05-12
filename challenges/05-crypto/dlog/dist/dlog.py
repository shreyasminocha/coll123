from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes, random
from sympy.ntheory.residue_ntheory import primitive_root
from secret import flag

p = getPrime(16)
g = primitive_root(p)

print(f"p = {p}")
print(f"g = {g}")

print("================")

alice_private = random.randrange(2, p - 1)
print(f"a = {alice_private}")

alice_public = pow(g, alice_private, p)
print(f"A = {alice_public}")

print("================")

bob_private = random.randrange(2, p - 1)

bob_public = pow(g, bob_private, p)
print(f"B = {bob_public}")

print("================")

shared_k = pow(bob_public, alice_private, p)
assert shared_k == pow(alice_public, bob_private, p)

guess = int(input("what's the shared secret: "))

if guess == shared_k:
    print(flag)
else:
    print("that's incorrect :(")
