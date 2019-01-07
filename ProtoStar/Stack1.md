# Stack1

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

    if(argc == 1) {
        errx(1, "please specify an argument\n");
    }

    modified = 0;
    strcpy(buffer, argv[1]);

    if(modified == 0x61626364) {
        printf("you have correctly got the variable to the right value\n");
    } else {
        printf("Try again, you got 0x%08x\n", modified);
    }
}
```

* Solution
```
(gdb) set disassembly-flavor intel
(gdb) disass main
Dump of assembler code for function main:
   0x0000000000401152 <+0>:	push   rbp
   0x0000000000401153 <+1>:	mov    rbp,rsp
   0x0000000000401156 <+4>:	sub    rsp,0x60
   0x000000000040115a <+8>:	mov    DWORD PTR [rbp-0x54],edi
   0x000000000040115d <+11>:	mov    QWORD PTR [rbp-0x60],rsi
   0x0000000000401161 <+15>:	cmp    DWORD PTR [rbp-0x54],0x1
   0x0000000000401165 <+19>:	jne    0x40117d <main+43>
   0x0000000000401167 <+21>:	lea    rsi,[rip+0xe9a]        # 0x402008
   0x000000000040116e <+28>:	mov    edi,0x1
   0x0000000000401173 <+33>:	mov    eax,0x0
   0x0000000000401178 <+38>:	call   0x401050 <errx@plt>
   0x000000000040117d <+43>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000401184 <+50>:	mov    rax,QWORD PTR [rbp-0x60]
   0x0000000000401188 <+54>:	add    rax,0x8
   0x000000000040118c <+58>:	mov    rdx,QWORD PTR [rax]
   0x000000000040118f <+61>:	lea    rax,[rbp-0x50]
   0x0000000000401193 <+65>:	mov    rsi,rdx
   0x0000000000401196 <+68>:	mov    rdi,rax
   0x0000000000401199 <+71>:	call   0x401030 <strcpy@plt>
   0x000000000040119e <+76>:	mov    eax,DWORD PTR [rbp-0x4]
   0x00000000004011a1 <+79>:	cmp    eax,0x61626364
   0x00000000004011a6 <+84>:	jne    0x4011b6 <main+100>
   0x00000000004011a8 <+86>:	lea    rdi,[rip+0xe79]        # 0x402028
   0x00000000004011af <+93>:	call   0x401040 <puts@plt>
   0x00000000004011b4 <+98>:	jmp    0x4011cc <main+122>
   0x00000000004011b6 <+100>:	mov    eax,DWORD PTR [rbp-0x4]
   0x00000000004011b9 <+103>:	mov    esi,eax
   0x00000000004011bb <+105>:	lea    rdi,[rip+0xe9d]        # 0x40205f
   0x00000000004011c2 <+112>:	mov    eax,0x0
   0x00000000004011c7 <+117>:	call   0x401060 <printf@plt>
   0x00000000004011cc <+122>:	mov    eax,0x0
   0x00000000004011d1 <+127>:	leave  
   0x00000000004011d2 <+128>:	ret    
End of assembler dump.
(gdb) b *main+79
Breakpoint 1 at 0x4011a1
(gdb) r 1234
Starting program: /root/Desktop/stack1 1234

Breakpoint 1, 0x00000000004011a1 in main ()
(gdb) cont
Continuing.
Try again, you got 0x00000000
[Inferior 1 (process 3156) exited normally]

(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/Desktop/stack1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Breakpoint 1, 0x00000000004011a1 in main ()
(gdb) x/30x $rsp
0x7fffffffe100:	0xffffe248	0x00007fff	0xffffe136	0x00000002
0x7fffffffe110:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe120:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe130:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe140:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe150:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe160:	0x00401100	0x00000000	0xf7e11b17	0x00007fff
0x7fffffffe170:	0x00000000	0x00000000
(gdb) x/x $rbp
0x7fffffffe160:	0x00401100
(gdb) info reg $eax
eax            0x41414141          1094795585
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/Desktop/stack1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB

Breakpoint 1, 0x00000000004011a1 in main ()
(gdb) x/30x $rsp
0x7fffffffe100:	0xffffe248	0x00007fff	0xffffe136	0x00000002
0x7fffffffe110:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe120:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe130:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe140:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffe150:	0x41414141	0x41414141	0x41414141	0x42424242
0x7fffffffe160:	0x00401100	0x00000000	0xf7e11b17	0x00007fff
0x7fffffffe170:	0x00000000	0x00000000
(gdb) x/x $rbp
0x7fffffffe160:	0x00401100
(gdb) info reg $eax
eax            0x42424242          1111638594
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAabcd
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/Desktop/stack1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAabcd

Breakpoint 1, 0x00000000004011a1 in main ()
(gdb) info reg $eax
eax            0x64636261          1684234849
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdcba
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/Desktop/stack1 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdcba

Breakpoint 1, 0x00000000004011a1 in main ()
(gdb) info reg $eax
eax            0x61626364          1633837924
(gdb) cont
Continuing.
you have correctly got the variable to the right value
[Inferior 1 (process 3155) exited normally]
(gdb) 
```
