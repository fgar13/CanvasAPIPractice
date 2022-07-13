import json
import requests

response = requests.get("https://canvas.instructure.com/api/v1/courses?access_token=<ACCESS-TOKEN>")

response = requests.get("https://canvas.instructure.com/api/v1/users/self?access_token=<ACCESS-TOKEN>")
print(response.text)

response = requests.get("https://canvas.instructure.com/api/v1/courses?access_token=7~<ACCESS-TOKEN>")
print(response.text)