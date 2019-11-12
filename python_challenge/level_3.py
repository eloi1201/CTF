import re, requests

url = "http://www.pythonchallenge.com/pc/def/equality.html"

res = requests.get(url)

res = res.text

regex_pattern = re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')

filtered_res = re.findall(regex_pattern, res)

plain_txt = ""

for entry in filtered_res:
	plain_txt = plain_txt + entry[4]

print(plain_txt)
