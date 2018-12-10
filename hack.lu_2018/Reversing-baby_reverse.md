# Baby reverse

### Question
```
Hey there!

Disclaimer: This chall is intended for new gamers only ;-)! You veterans got plenty of other Challenges which will keep you busy, so please pass this Challenge to someone, who never or rarely reversed before! We encourage everyone who never reversed anything to try this challenge. We believe in you and your future reversing skills =). You CAN do it!

The task is to find the correct input which will be the flag. See the challenge files for more instructions.
```

### File information
```
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$ checksec chall
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/eloi/.pwntools-cache/update to 'never'.
[*] A newer version of pwntools is available on pypi (3.10.0b2 --> 3.13.0b0).
    Update with: $ pip install -U pwntools==3.13.0b0
[*] '/home/eloi/ctf/hack.lu_2018/chall'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400080)
    RWX:      Has RWX segments
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$ ./chall
Welcome to this Chall!
Enter the Key to win: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$
```

### File analysis
```
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x400092 --> 0xf48050fcfff2e2c 
RDX: 0x2e ('.')
RSI: 0x4000d7 ("Welcome to this Chall! \nEnter the Key to win: ")
RDI: 0x0 
RBP: 0x0 
RSP: 0x7fffffffe250 --> 0x1 
RIP: 0x400096 --> 0x48017eb60f48050f 
R8 : 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x302 
R12: 0x0 
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x400090:	syscall 
   0x400092:	sub    al,0x2e
   0x400094:	dec    edi
=> 0x400096:	syscall 
   0x400098:	movzx  rdi,BYTE PTR [rsi+0x1]
   0x40009d:	xor    QWORD PTR [rsi],rdi
   0x4000a0:	inc    rsi
   0x4000a3:	dec    rdx
No argument
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe250 --> 0x1 
0008| 0x7fffffffe258 --> 0x7fffffffe4df ("/home/eloi/ctf/hack.lu_2018/chall")
0016| 0x7fffffffe260 --> 0x0 
0024| 0x7fffffffe268 --> 0x7fffffffe501 ("LC_PAPER=ko_KR.UTF-8")
0032| 0x7fffffffe270 --> 0x7fffffffe516 ("XDG_SESSION_ID=181")
0040| 0x7fffffffe278 --> 0x7fffffffe529 ("LC_ADDRESS=ko_KR.UTF-8")
0048| 0x7fffffffe280 --> 0x7fffffffe540 ("LC_MONETARY=ko_KR.UTF-8")
0056| 0x7fffffffe288 --> 0x7fffffffe558 ("VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0000000000400096 in ?? ()
gdb-peda$ s
```

```
[----------------------------------registers-----------------------------------]
RAX: 0x25 ('%')
RBX: 0x0 
RCX: 0x400098 --> 0x3e3148017eb60f48 
RDX: 0x2e ('.')
RSI: 0x4000d7 ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n to win: ")
RDI: 0x0 
RBP: 0x0 
RSP: 0x7fffffffe250 --> 0x1 
RIP: 0x400098 --> 0x3e3148017eb60f48 
R8 : 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x346 
R12: 0x0 
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x400092:	sub    al,0x2e
   0x400094:	dec    edi
   0x400096:	syscall 
=> 0x400098:	movzx  rdi,BYTE PTR [rsi+0x1]
   0x40009d:	xor    QWORD PTR [rsi],rdi
   0x4000a0:	inc    rsi
   0x4000a3:	dec    rdx
   0x4000a6:	jne    0x400098
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe250 --> 0x1 
0008| 0x7fffffffe258 --> 0x7fffffffe4df ("/home/eloi/ctf/hack.lu_2018/chall")
0016| 0x7fffffffe260 --> 0x0 
0024| 0x7fffffffe268 --> 0x7fffffffe501 ("LC_PAPER=ko_KR.UTF-8")
0032| 0x7fffffffe270 --> 0x7fffffffe516 ("XDG_SESSION_ID=181")
0040| 0x7fffffffe278 --> 0x7fffffffe529 ("LC_ADDRESS=ko_KR.UTF-8")
0048| 0x7fffffffe280 --> 0x7fffffffe540 ("LC_MONETARY=ko_KR.UTF-8")
0056| 0x7fffffffe288 --> 0x7fffffffe558 ("VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0000000000400098 in ?? ()
gdb-peda$ 
```

```
[----------------------------------registers-----------------------------------]
RAX: 0x25 ('%')
RBX: 0x0 
RCX: 0x400098 --> 0x3e3148017eb60f48 
RDX: 0x2e ('.')
RSI: 0x4000d7 ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n to win: ")
RDI: 0x42 ('B')
RBP: 0x0 
RSP: 0x7fffffffe250 --> 0x1 
RIP: 0x40009d --> 0xff48c6ff483e3148 
R8 : 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x346 
R12: 0x0 
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x400094:	dec    edi
   0x400096:	syscall 
   0x400098:	movzx  rdi,BYTE PTR [rsi+0x1]
=> 0x40009d:	xor    QWORD PTR [rsi],rdi
   0x4000a0:	inc    rsi
   0x4000a3:	dec    rdx
   0x4000a6:	jne    0x400098
   0x4000a8:	and    ecx,0x2e
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe250 --> 0x1 
0008| 0x7fffffffe258 --> 0x7fffffffe4df ("/home/eloi/ctf/hack.lu_2018/chall")
0016| 0x7fffffffe260 --> 0x0 
0024| 0x7fffffffe268 --> 0x7fffffffe501 ("LC_PAPER=ko_KR.UTF-8")
0032| 0x7fffffffe270 --> 0x7fffffffe516 ("XDG_SESSION_ID=181")
0040| 0x7fffffffe278 --> 0x7fffffffe529 ("LC_ADDRESS=ko_KR.UTF-8")
0048| 0x7fffffffe280 --> 0x7fffffffe540 ("LC_MONETARY=ko_KR.UTF-8")
0056| 0x7fffffffe288 --> 0x7fffffffe558 ("VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x000000000040009d in ?? ()
gdb-peda$ 
```
Binary runs XOR operation (input[i]^input[i+1]) after taking 46(0x2e) bytes of strings.

The XOR result will be compared to strings in 0x40010C location through cmps function

```
[----------------------------------registers-----------------------------------]
RAX: 0x2e ('.')
RBX: 0x0 
RCX: 0x2e ('.')
RDX: 0x0 
RSI: 0x4000d7 --> 0x544508020c0f0957 
RDI: 0x40010c --> 0x261838221c060d0a 
RBP: 0x0 
RSP: 0x7fffffffe250 --> 0x1 
RIP: 0x4000b6 --> 0x344975c98548a6f3 
R8 : 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x346 
R12: 0x0 
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4000ab:	add    cl,0x26
   0x4000ae:	lea    rdi,[rsi+0x7]
   0x4000b2:	lea    rsi,[rdi-0x35]
=> 0x4000b6:	repz cmps BYTE PTR ds:[rsi],BYTE PTR es:[rdi]
   0x4000b8:	test   rcx,rcx
   0x4000bb:	jne    0x400106
   0x4000bd:	xor    al,0x2f
   0x4000bf:	push   0x21796159
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe250 --> 0x1 
0008| 0x7fffffffe258 --> 0x7fffffffe4df ("/home/eloi/ctf/hack.lu_2018/chall")
0016| 0x7fffffffe260 --> 0x0 
0024| 0x7fffffffe268 --> 0x7fffffffe501 ("LC_PAPER=ko_KR.UTF-8")
0032| 0x7fffffffe270 --> 0x7fffffffe516 ("XDG_SESSION_ID=181")
0040| 0x7fffffffe278 --> 0x7fffffffe529 ("LC_ADDRESS=ko_KR.UTF-8")
0048| 0x7fffffffe280 --> 0x7fffffffe540 ("LC_MONETARY=ko_KR.UTF-8")
0056| 0x7fffffffe288 --> 0x7fffffffe558 ("VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x00000000004000b6 in ?? ()
gdb-peda$ 
```


### Decryption code 
```
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$ cat solve.py
encFlag = "0A 0D 06 1C 22 38 18 26 36 0F 39 2B  1C 59 42 2C 36 1A 2C 26 1C 17 2D 39 57 43 01 07  2B 38 09 07 1A 01 17 13 13 17 2D 39 0A 0D 06 46  5C 7D".split()
tmp = int(encFlag[-1], 16)
decFlag = ""
for i in range(len(encFlag)-1, 0, -1):
        tmp = tmp ^ int(encFlag[i-1], 16)
        decFlag = decFlag + chr(tmp)

print decFlag[::-1] + '}'
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$
```

### Flag
```
eloi@null2root-ubuntu:~/ctf/hack.lu_2018$ python solve.py
flag{Yay_if_th1s_is_yer_f1rst_gnisrever_flag!}
```
