# Parts of the code are borrowed from Engineer Man
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

names = json.loads(open('names_PL.json').read())
surnames = json.loads(open('surnames_PL.json').read())
mail_providers = ['wp.pl', 'onet.pl', 'gazeta.pl', 'o2.pl', 'gmail.com', 'interia.pl', 'poczta.fm', 'op.pl', 'vp.pl', 'int.pl', 'live.com', 'outlook.com']

for name in names:

	surname = ''.join(random.choice(surnames))
	name_extra = ''.join(random.choice(string.digits))
	mail_provider = ''.join(random.choice(mail_providers))

	
# Generate random e-mail for login

	username = name.lower() + '.' + surname.lower() + name_extra + '@' + mail_provider
	password = ''.join(random.choice(chars) for i in range(8))

# You need to get proper data strings from "Form Data" in headers

	requests.post(url, allow_redirects=False, data={
		'find_it_in_request': username,
		'find_it_in_request': password
	})

	print('Sending username %s and password %s' % (username, password))
