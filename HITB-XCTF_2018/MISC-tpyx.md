# MISC-tpyx

<img width="895" alt="screen shot 2018-04-21 at 2 33 48 pm" src="https://user-images.githubusercontent.com/14992494/39082594-51682488-4588-11e8-86c4-15ae0678b5b1.png">

Downloaded png file had broken image structure. The png file didn't open properly even recovered CRC value. So binwalk tool was used to export hidden bianry.

```
root@kali:~/Desktop/xctf# pngcheck e47c7307-b54c-4316-9894-5a8daec738b4.png 
e47c7307-b54c-4316-9894-5a8daec738b4.png  CRC error in chunk IDAT (computed ecfb2a19, expected ba3de214)
ERROR: e47c7307-b54c-4316-9894-5a8daec738b4.png
```

```
root@kali:~/Desktop/xctf# binwalk e47c7307-b54c-4316-9894-5a8daec738b4.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1024 x 653, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression

root@kali:~/Desktop/xctf# binwalk -e e47c7307-b54c-4316-9894-5a8daec738b4.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1024 x 653, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression

root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted# binwalk -e 29

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
2675341       0x28D28D        Zlib compressed data, best compression
```

The ASCII text file was found which comprised of HEX value after a few attempts of binwalk.

```
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# ls
28D28D  28D28D.zlib
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# file 28D28D
28D28D: ASCII text, with very long lines, with no line terminators
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# cat 28D28D
377abcaf271c000382f96c91300000000000000073000000000000003c0e24409c429fdb08f31ebc2361b3016f04a79a070830334c68dd47db383e4b7246acad87460cd00ba62cfae68508182a69527a0104060001093000070b0100022406f107010a5307cb7afbfaec5aa07623030101055d0000010001000c2c2700080a01c35b933000000501110b0066006c00610067000000120a010000844bf3571cd101130a010000e669e866d1d301140a010080ffcdd963d1d301150601008000000000001800345172634f556d365761752b5675425838672b4950673d3d
```

The HEX string was hexdump of 7z file which has password string at end of the 7z file.

```
Python 2.7.14+ (default, Feb  6 2018, 19:12:18) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> encStr = "377abcaf271c000382f96c91300000000000000073000000000000003c0e24409c429fdb08f31ebc2361b3016f04a79a070830334c68dd47db383e4b7246acad87460cd00ba62cfae68508182a69527a0104060001093000070b0100022406f107010a5307cb7afbfaec5aa07623030101055d0000010001000c2c2700080a01c35b933000000501110b0066006c00610067000000120a010000844bf3571cd101130a010000e669e866d1d301140a010080ffcdd963d1d301150601008000000000001800345172634f556d365761752b5675425838672b4950673d3d"
>>> encStr.decode("hex")
"7z\xbc\xaf'\x1c\x00\x03\x82\xf9l\x910\x00\x00\x00\x00\x00\x00\x00s\x00\x00\x00\x00\x00\x00\x00<\x0e$@\x9cB\x9f\xdb\x08\xf3\x1e\xbc#a\xb3\x01o\x04\xa7\x9a\x07\x0803Lh\xddG\xdb8>KrF\xac\xad\x87F\x0c\xd0\x0b\xa6,\xfa\xe6\x85\x08\x18*iRz\x01\x04\x06\x00\x01\t0\x00\x07\x0b\x01\x00\x02$\x06\xf1\x07\x01\nS\x07\xcbz\xfb\xfa\xecZ\xa0v#\x03\x01\x01\x05]\x00\x00\x01\x00\x01\x00\x0c,'\x00\x08\n\x01\xc3[\x930\x00\x00\x05\x01\x11\x0b\x00f\x00l\x00a\x00g\x00\x00\x00\x12\n\x01\x00\x00\x84K\xf3W\x1c\xd1\x01\x13\n\x01\x00\x00\xe6i\xe8f\xd1\xd3\x01\x14\n\x01\x00\x80\xff\xcd\xd9c\xd1\xd3\x01\x15\x06\x01\x00\x80\x00\x00\x00\x00\x00\x18\x004QrcOUm6Wau+VuBX8g+IPg=="
>>> open("flag", "wb").write(encStr.decode("hex"))
```
```
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# xxd flag 
00000000: 377a bcaf 271c 0003 82f9 6c91 3000 0000  7z..'.....l.0...
00000010: 0000 0000 7300 0000 0000 0000 3c0e 2440  ....s.......<.$@
00000020: 9c42 9fdb 08f3 1ebc 2361 b301 6f04 a79a  .B......#a..o...
00000030: 0708 3033 4c68 dd47 db38 3e4b 7246 acad  ..03Lh.G.8>KrF..
00000040: 8746 0cd0 0ba6 2cfa e685 0818 2a69 527a  .F....,.....*iRz
00000050: 0104 0600 0109 3000 070b 0100 0224 06f1  ......0......$..
00000060: 0701 0a53 07cb 7afb faec 5aa0 7623 0301  ...S..z...Z.v#..
00000070: 0105 5d00 0001 0001 000c 2c27 0008 0a01  ..].......,'....
00000080: c35b 9330 0000 0501 110b 0066 006c 0061  .[.0.......f.l.a
00000090: 0067 0000 0012 0a01 0000 844b f357 1cd1  .g.........K.W..
000000a0: 0113 0a01 0000 e669 e866 d1d3 0114 0a01  .......i.f......
000000b0: 0080 ffcd d963 d1d3 0115 0601 0080 0000  .....c..........
000000c0: 0000 0018 0034 5172 634f 556d 3657 6175  .....4QrcOUm6Wau
000000d0: 2b56 7542 5838 672b 4950 673d 3d         +VuBX8g+IPg==
```

<img width="600" alt="screen shot 2018-04-21 at 5 03 05 pm" src="https://user-images.githubusercontent.com/14992494/39082692-b7aa82f8-4589-11e8-816d-056f797a63b8.png">

### Flag
HITB{0c88d56694c2fb3bcc416e122c1072eb}
