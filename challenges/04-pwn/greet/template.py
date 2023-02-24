from pwn import *

r = remote("123.sec.rice.edu", 50610)
r.recvline()

r.sendline(b"john")
sys.stdout.write(r.recvall())
