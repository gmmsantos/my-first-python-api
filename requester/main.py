import requests

url = "http://127.0.0.1:5000/total_salary"

myrequest = requests.get(url)

print(myrequest)
print(myrequest.json())
