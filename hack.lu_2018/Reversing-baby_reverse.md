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
