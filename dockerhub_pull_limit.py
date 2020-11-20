#!/usr/bin/env python

# Obtain the number of remaining pulls from Docker Hub
# Compatible with Python 2 and 3

from __future__ import print_function
import requests
import sys

URL = "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull"
REGISTRY_URL = "https://registry-1.docker.io/v2/ratelimitpreview/test/manifests/latest"

resp = requests.get(URL)
resp.raise_for_status()
token = resp.json().get('token')

request_headers = { 'Authorization': 'Bearer ' + token }
response = requests.head(REGISTRY_URL, headers=request_headers)
response.raise_for_status()
headers = response.headers

if "RateLimit-Limit" not in headers or "RateLimit-Remaining" not in headers:
    print("Couldn't obtain rate limit information", file=sys.stderr)
    exit(1)

pulls_limit = headers["RateLimit-Limit"].split(";")[0]
pulls_remaining = headers["RateLimit-Remaining"].split(";")[0]

time_window = headers["RateLimit-Limit"].split(";")[1].split("=")[-1]

print("Remaining Docker Hub pull requests: %s/%s" % (pulls_remaining, pulls_limit))
print("Time window: %s s" % time_window)

if "RateLimit-Reset" in headers:
    ratelimit_reset = headers["RateLimit-Reset"]
    print("Time till limit reset: %s s" % ratelimit_reset)
