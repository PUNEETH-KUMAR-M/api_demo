import requests
age=30
sex='F'
response=requests.get(f"http://127.0.0.1:8000/predict?age={age}&sex={sex}")
output= response.json()
print(output)