import requests
import json
import jq
import jwt

URL = "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull"
response = requests.get(URL)
if response.status_code != 200:
   print("Failed to get a response from Docker Hub")
   exit(1)
output = jq.compile(".token").input(json.loads(response.text)).text()
output = output[1:-1]

if hasattr(jwt, 'decode'):
    # PyJWT
    decoded = jwt.decode(output, verify=False)
elif hasattr(jwt, 'JWT'):
    # jwt
    decoded = jwt.JWT().decode(output, do_verify=False)
else:
    print("Unknown jwt module")
    exit(1)

pull_limit = decoded['access'][0]['parameters']['pull_limit']
print("Remaining pulls:", pull_limit)
