#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    item = parse.urlencode(val)
    item = item.encode('ascii')
    reques = request.Request(sys.argv[1], item)
    with request.urlopen(reques) as response:
        body = response.read()
        print(body.decode('utf-8'))
