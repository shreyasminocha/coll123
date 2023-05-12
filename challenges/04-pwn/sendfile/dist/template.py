assembly = '''
    mov rax, ??? /* open */
    lea rdi, [rip + flag]
    mov rsi, 0 /* <mode> = O_RDONLY */
    syscall

    mov rsi, rax /* <in_fd> */
    mov rdi, 1 /* <out_fd> = fileno(stdout) */
    mov rdx, ??? /* <offset> */
    mov r10, ??? /* <count> */
    mov rax, ??? /* sendfile */
    syscall

    flag:
    .string "./flag.txt"
'''
