# MISC-tpyx

root@kali:~/Desktop/xctf# pngcheck e47c7307-b54c-4316-9894-5a8daec738b4.png 
e47c7307-b54c-4316-9894-5a8daec738b4.png  CRC error in chunk IDAT (computed ecfb2a19, expected ba3de214)
ERROR: e47c7307-b54c-4316-9894-5a8daec738b4.png

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

root@kali:~/Desktop/xctf# cd _e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted# ls
29  29.zlib
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted# binwalk -e 29

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
2675341       0x28D28D        Zlib compressed data, best compression

root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted# ls
29  _29.extracted  29.zlib
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted# cd _29.extracted/
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# ls
28D28D  28D28D.zlib
root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# file 28D28D
28D28D: ASCII text, with very long lines, with no line terminators


root@kali:~/Desktop/xctf/_e47c7307-b54c-4316-9894-5a8daec738b4.png.extracted/_29.extracted# cat 28D28D
377abcaf271c000382f96c91300000000000000073000000000000003c0e24409c429fdb08f31ebc2361b3016f04a79a070830334c68dd47db383e4b7246acad87460cd00ba62cfae68508182a69527a0104060001093000070b0100022406f107010a5307cb7afbfaec5aa07623030101055d0000010001000c2c2700080a01c35b933000000501110b0066006c00610067000000120a010000844bf3571cd101130a010000e669e866d1d301140a010080ffcdd963d1d301150601008000000000001800345172634f556d365761752b5675425838672b4950673d3d

Python 2.7.14+ (default, Feb  6 2018, 19:12:18) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> encStr = "377abcaf271c000382f96c91300000000000000073000000000000003c0e24409c429fdb08f31ebc2361b3016f04a79a070830334c68dd47db383e4b7246acad87460cd00ba62cfae68508182a69527a0104060001093000070b0100022406f107010a5307cb7afbfaec5aa07623030101055d0000010001000c2c2700080a01c35b933000000501110b0066006c00610067000000120a010000844bf3571cd101130a010000e669e866d1d301140a010080ffcdd963d1d301150601008000000000001800345172634f556d365761752b5675425838672b4950673d3d"
>>> encStr.decode("hex")
"7z\xbc\xaf'\x1c\x00\x03\x82\xf9l\x910\x00\x00\x00\x00\x00\x00\x00s\x00\x00\x00\x00\x00\x00\x00<\x0e$@\x9cB\x9f\xdb\x08\xf3\x1e\xbc#a\xb3\x01o\x04\xa7\x9a\x07\x0803Lh\xddG\xdb8>KrF\xac\xad\x87F\x0c\xd0\x0b\xa6,\xfa\xe6\x85\x08\x18*iRz\x01\x04\x06\x00\x01\t0\x00\x07\x0b\x01\x00\x02$\x06\xf1\x07\x01\nS\x07\xcbz\xfb\xfa\xecZ\xa0v#\x03\x01\x01\x05]\x00\x00\x01\x00\x01\x00\x0c,'\x00\x08\n\x01\xc3[\x930\x00\x00\x05\x01\x11\x0b\x00f\x00l\x00a\x00g\x00\x00\x00\x12\n\x01\x00\x00\x84K\xf3W\x1c\xd1\x01\x13\n\x01\x00\x00\xe6i\xe8f\xd1\xd3\x01\x14\n\x01\x00\x80\xff\xcd\xd9c\xd1\xd3\x01\x15\x06\x01\x00\x80\x00\x00\x00\x00\x00\x18\x004QrcOUm6Wau+VuBX8g+IPg=="
>>> open("flag", "wb").write(encStr.decode("hex"))

### Flag
HITB{0c88d56694c2fb3bcc416e122c1072eb}
