
import requests
acces_key="74070f5c32d113f4c2601fe638efe119"
#Access_key "74070f5c32d113f4c2601fe638efe119"

url = "https://api.aviationstack.com/v1/flights" 


response = requests.get(url)

print(response.json())
