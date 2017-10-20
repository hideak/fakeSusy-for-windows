# Request for a website

import ssl
from urllib.request import urlopen

context = ssl._create_unverified_context()
site = urlopen('https://susy.ic.unicamp.br:9999/mc102uvxz/05/dados/arq01.in', context=context)
text = site.read()
text = text.decode('utf-8')
