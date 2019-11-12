import re, requests

def url_request(param):

	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}".format(param)

	res = requests.get(url)

	return res.text

index = 0

while(1):

	if index == 0:

		param = "12345"

	res = url_request(param)

	if "next" in res:

		index = int(param)

		param = res.split(" ")[-1]

	elif "Divide" in res:

		res = url_request(str(index/2))

		param = res.split(" ")[-1]

	else:

		print(res)

		break
