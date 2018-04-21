# MISC-pix

<img width="892" alt="screen shot 2018-04-21 at 6 11 40 pm" src="https://user-images.githubusercontent.com/14992494/39083472-d27a4ef8-4596-11e8-9d08-50c3fd45432d.png">

The question file was an image file which contains Keepass password database file.

```
root@kali:~/Desktop/xctf# zsteg aee487a2-49cd-4f1f-ada6-b2d398342d99.SteinsGate 
imagedata           .. text: " !#865   "
b1,r,msb,xy         .. text: "y5b@2~2t"
b1,rgb,lsb,xy       .. file: Keepass password database 2.x KDBX
b2,r,msb,xy         .. text: "\rP`I$X7D"
b2,bgr,lsb,xy       .. text: "b;d'8H~M"
b4,g,msb,xy         .. text: ";pTr73& dvG:"

root@kali:~/Desktop/xctf# zsteg aee487a2-49cd-4f1f-ada6-b2d398342d99.SteinsGate -E b1,rgb,lsb,xy > passwd.db

root@kali:~/Desktop/xctf# file passwd.db 
passwd.db: Keepass password database 2.x KDBX
```

Based on the question description, the password db file had a weak password which combined with "hitb" and 6 digit numbers. So developed simple python code to genenrate a dictionary file.

```
initStr = "hitb"

for i in range(0, 1000000):
    print initStr + "%06d" %i
```

Keepass2 password db can be cracked by john the ripper, but it requires hash data of the target password db. The hash data was acquired by using keepass2john tool. 

```
root@kali:~/Desktop/xctf# keepass2john passwd.db 
passwd.db:$keepass$*2*6000*222*774fbe05c37a98c8094e1d625d285a193ae9cf9bc7f6ccbf8ee5cb28e2894070*02207c3d0a3feb6a589dc84f8d73ff86fe2629ff25f9cf23f7f9545b5786f882*065f70730c4e7b98ef7ea869f6958b03*2b3d24717d3e284484af4171a4a752d688111a96f7c36e7233048fc028867f16*43dbb269dff30e5cd1ce74dd8527594004f49bcd17414c24cb22c0d6e2b26a0b

root@kali:~/Desktop/xctf# keepass2john passwd.db > passwd_hash.db

root@kali:~/Desktop/xctf# john --wordlist=./dic.txt passwd_hash.db
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64 OpenSSL])
Press 'q' or Ctrl-C to abort, almost any other key for status
hitb180408       (passwd.db)
1g 0:00:02:45 DONE (2018-04-21 06:51) 0.006039g/s 1089p/s 1089c/s 1089C/s hitb180408
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

"hitb180408" is the password to open the keepass2 password db. A flag was found after opening the password db file with the password.

<img width="553" alt="screen shot 2018-04-21 at 7 02 06 pm" src="https://user-images.githubusercontent.com/14992494/39083480-f36c92ec-4596-11e8-9406-e03e3944b33c.png">
<img width="634" alt="screen shot 2018-04-21 at 7 02 46 pm" src="https://user-images.githubusercontent.com/14992494/39083484-f6e1453a-4596-11e8-9155-68cc60c8f253.png">


### Flag
HITB{p1x_aNd_k33pass}


<img width="292" alt="screen shot 2018-04-21 at 7 07 20 pm" src="https://user-images.githubusercontent.com/14992494/39083723-b1d9f3a6-459b-11e8-919b-fb6851e8a89d.png">
