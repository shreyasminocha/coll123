import random
import string
from secret import flag

print("please pack some ints for me (ps: there are over 500)")

for _ in range(0x200):
    cs = random.choices(string.ascii_lowercase, k=10)
    s = "".join(cs)
    bs = s.encode("utf-8")

    print(int.from_bytes(bs, "little"))
    submission = input().strip()

    if s != submission:
        print("that's incorrect. try again")
        exit(1)

print(f"flag = {flag}")
