# Question



```
Null2Root:~ eloi$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> encStr = "Anyo!e!howouldsacrificepo!icyforexecu!!onspeedthink!securityisacomm!ditytop!urintoasy!tem!"
>>> encList = encStr.split("!")
>>> encList
['Anyo', 'e', 'howouldsacrificepo', 'icyforexecu', '', 'onspeedthink', 'securityisacomm', 'ditytop', 'urintoasy', 'tem', '']
>>> for i in range(len(encList)):
...     print len(encList[i]),
... 
4 1 18 11 0 12 15 7 9 3 0
>>> for i in range(len(encList)):
...     print chr(len(encList[i])+96),
... 
d a r k ` l o g i c `
>>> 

```

# Flag

dark logic
