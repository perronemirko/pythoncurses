import sys
import requests
import socket
import json

if len(sys.argv) < 2 :
  print("usage: " + sys.argv[0] + " <url>")
  sys.exit(1)
  
req = requests.get(f"https://{sys.argv[1]}")
print(f"\n {str(req.headers)}")

getHostBy_ = socket.gethostbyname(sys.argv[1])
print(f"\nThe IP address of {sys.argv[1]} is {getHostBy_} \n")

req_two = requests.get(f"https://ipinfo.io/{getHostBy_}/json")
resp_ = json.loads(req_two.text)

print(f"Location => {resp_['loc']}")
print(f"Region => {resp_['region']} ")
print(f"City => {resp_['city']}")
print(f"Country => {resp_['country'] }")


