from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from secret import flag

KEY_SIZE = 1024
e = 5

m = bytes_to_long(flag)


while True:
    p = getPrime(KEY_SIZE)
    q = getPrime(KEY_SIZE)
    n = p * q

    assert m < n

    phi = (p - 1) * (q - 1)

    try:
        d = pow(e, -1, phi)
    except:
        continue

    c = pow(m, e, n)

    print(f"n = {n}")
    print(f"e = {e}")
    print(f"c = {c}")

    break
