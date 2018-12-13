### Credential
```
level7 / come together
```

### Solution
```
[level7@ftz level7]$ ls
hint  public_html  tmp

[level7@ftz level7]$ cat hint 


/bin/level7 명령을 실행하면, 패스워드 입력을 요청한다.

1. 패스워드는 가까운곳에..
2. 상상력을 총동원하라.
3. 2진수를 10진수를 바꿀 수 있는가?
4. 계산기 설정을 공학용으로 바꾸어라.

[level7@ftz level7]$ /bin/level7         
Insert The Password : 1234
cat: /bin/wrong.txt: No such file or directory

(gdb) disass main
Dump of assembler code for function main:
0x08048454 <main+0>:	push   %ebp
0x08048455 <main+1>:	mov    %esp,%ebp
0x08048457 <main+3>:	sub    $0x8,%esp
0x0804845a <main+6>:	and    $0xfffffff0,%esp
0x0804845d <main+9>:	mov    $0x0,%eax
0x08048462 <main+14>:	sub    %eax,%esp
0x08048464 <main+16>:	sub    $0xc,%esp
0x08048467 <main+19>:	push   $0x64
0x08048469 <main+21>:	call   0x8048344 <malloc>
0x0804846e <main+26>:	add    $0x10,%esp
0x08048471 <main+29>:	mov    %eax,0xfffffffc(%ebp)
0x08048474 <main+32>:	sub    $0xc,%esp
0x08048477 <main+35>:	push   $0x80485c0
0x0804847c <main+40>:	call   0x8048384 <printf>
0x08048481 <main+45>:	add    $0x10,%esp
0x08048484 <main+48>:	sub    $0x4,%esp
0x08048487 <main+51>:	pushl  0x8049744
0x0804848d <main+57>:	push   $0x64
0x0804848f <main+59>:	pushl  0xfffffffc(%ebp)
0x08048492 <main+62>:	call   0x8048354 <fgets>
0x08048497 <main+67>:	add    $0x10,%esp
0x0804849a <main+70>:	sub    $0x4,%esp
---Type <return> to continue, or q <return> to quit---
0x0804849d <main+73>:	push   $0x4
0x0804849f <main+75>:	push   $0x80485d7
0x080484a4 <main+80>:	pushl  0xfffffffc(%ebp)
0x080484a7 <main+83>:	call   0x8048364 <strncmp>
0x080484ac <main+88>:	add    $0x10,%esp
0x080484af <main+91>:	test   %eax,%eax
0x080484b1 <main+93>:	jne    0x80484cd <main+121>
0x080484b3 <main+95>:	sub    $0xc,%esp
0x080484b6 <main+98>:	push   $0x80485e0
0x080484bb <main+103>:	call   0x8048384 <printf>
0x080484c0 <main+108>:	add    $0x10,%esp
0x080484c3 <main+111>:	sub    $0xc,%esp
0x080484c6 <main+114>:	push   $0x0
0x080484c8 <main+116>:	call   0x8048394 <exit>
0x080484cd <main+121>:	sub    $0xc,%esp
0x080484d0 <main+124>:	push   $0x8048617
0x080484d5 <main+129>:	call   0x8048334 <system>
0x080484da <main+134>:	add    $0x10,%esp
0x080484dd <main+137>:	leave  
0x080484de <main+138>:	ret    
0x080484df <main+139>:	nop    
End of assembler dump.
(gdb) x/s 0x80485c0  
0x80485c0 <_IO_stdin_used+28>:	 "Insert The Password : "
(gdb) x/s 0x80485d7
0x80485d7 <_IO_stdin_used+51>:	 "mate"
(gdb) x/s 0x80485e0
0x80485e0 <_IO_stdin_used+60>:	 "\nCongratulation! next password is \"break the world\".\n\n"
(gdb) quit

[root@ftz level7]$ /bin/level7
Insert The Password : mate

Congratulation! next password is "break the world".

```
