# Stack0

* Source code

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    volatile int modified;
    char buffer[64];

    modified = 0;
    gets(buffer);

    if(modified != 0) {
        printf("you have changed the 'modified' variable\n");
    } else {
        printf("Try again?\n");
    }
}
```

* Solution

```
(gdb) set disassembly-flavor intel
(gdb) disass main
Dump of assembler code for function main:
   0x0000000000401132 <+0>:	push   rbp
   0x0000000000401133 <+1>:	mov    rbp,rsp
   0x0000000000401136 <+4>:	sub    rsp,0x60
   0x000000000040113a <+8>:	mov    DWORD PTR [rbp-0x54],edi
   0x000000000040113d <+11>:	mov    QWORD PTR [rbp-0x60],rsi
   0x0000000000401141 <+15>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000401148 <+22>:	lea    rax,[rbp-0x50]
   0x000000000040114c <+26>:	mov    rdi,rax
   0x000000000040114f <+29>:	mov    eax,0x0
   0x0000000000401154 <+34>:	call   0x401040 <gets@plt>
   0x0000000000401159 <+39>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040115c <+42>:	test   eax,eax
   0x000000000040115e <+44>:	je     0x40116e <main+60>
   0x0000000000401160 <+46>:	lea    rdi,[rip+0xea1]        # 0x402008
   0x0000000000401167 <+53>:	call   0x401030 <puts@plt>
   0x000000000040116c <+58>:	jmp    0x40117a <main+72>
   0x000000000040116e <+60>:	lea    rdi,[rip+0xebc]        # 0x402031
   0x0000000000401175 <+67>:	call   0x401030 <puts@plt>
   0x000000000040117a <+72>:	mov    eax,0x0
   0x000000000040117f <+77>:	leave  
   0x0000000000401180 <+78>:	ret    
End of assembler dump.
(gdb) b *main+42
Breakpoint 1 at 0x40115c
(gdb) run 
Starting program: /root/Desktop/stack0 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x000000000040115c in main ()
(gdb) info reg $eax
eax            0x0                 0
(gdb) x/30x $rsp
0x7fffffffe150:	0xffffe298	0x00007fff	0xffffe186	0x00000001
0x7fffffffe160:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe170:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe180:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe190:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe1a0:	0x61616161	0x61616161	0x61616161	0x00000000
0x7fffffffe1b0:	0x00401190	0x00000000	0xf7e11b17	0x00007fff
0x7fffffffe1c0:	0x00000000	0x00000000
(gdb) x/x $rbp
0x7fffffffe1b0:	0x00401190
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/Desktop/stack0 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbb

Breakpoint 1, 0x000000000040115c in main ()
(gdb) info reg $eax
eax            0x62626262          1650614882
(gdb) x/30x $rsp
0x7fffffffe150:	0xffffe298	0x00007fff	0xffffe186	0x00000001
0x7fffffffe160:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe170:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe180:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe190:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffe1a0:	0x61616161	0x61616161	0x61616161	0x62626262
0x7fffffffe1b0:	0x00401100	0x00000000	0xf7e11b17	0x00007fff
0x7fffffffe1c0:	0x00000000	0x00000000
(gdb) x/x $rbp
0x7fffffffe1b0:	0x00401100
(gdb) cont
Continuing.
you have changed the 'modified' variable
[Inferior 1 (process 2992) exited normally]
(gdb) 
```
