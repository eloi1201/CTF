import re, requests, string

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

res = requests.get(url)

res = res.text

patt = re.compile('[^a-zA-Z0-9. <]{1}[a-z]{1}[^a-zA-Z0-9. >]{1}')

res = re.findall(patt, res)

plain_txt = ""

for line in res:

	for entry in line:

		if entry.isalpha() == True:

			plain_txt = plain_txt + entry

print(plain_txt)
