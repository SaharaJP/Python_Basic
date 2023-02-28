import requests
import re


req = requests.get('http://www.columbia.edu/~fdc/sample.html')
result = re.findall(r'>(.+)</h3>', req.text)
print(result)
