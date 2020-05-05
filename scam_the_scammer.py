# The code is borrowed from Engineer Man
import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# You need to open your browser's devtools, fill the form, send it and find the url where the form is send to.
# (in Chrome "Request URL" is your target, Request method is POST and "Form Data" is used in code below)

url = 'http://your.target.tld/find_it_in_dev_tools.php'

names = json.loads(open('names_EN.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

# Generate random e-mail for login
# TODO: add more e-mail providers

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

# You need to get proper data strings from "Form Data" in headers

	requests.post(url, allow_redirects=False, data={
		'find_it_in_request': username,
		'find_it_in_request': password
	})

	print 'Sending username %s and password %s' % (username, password)
