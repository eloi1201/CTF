import re, requests, string

url = "http://www.pythonchallenge.com/pc/def/map.html"

res = requests.get(url)

res = res.text

patt = re.compile('<font color="#f000f0">\n.*\n</tr></td>')

cipher_txt = re.findall(patt, res)

cipher_txt = cipher_txt[0].split("\n")[1]

plain_txt = ""

for entry in cipher_txt:

   if entry.isalpha() == True:

      ascii_num = ord(entry) + 2

      entry = chr(ascii_num)      

      if entry.islower():

         plain_txt = plain_txt + entry

      else:

         ascii_num = ord(entry) - 26

         entry = chr(ascii_num)      

         plain_txt = plain_txt + entry

   else:

      plain_txt = plain_txt + entry

print(plain_txt)
