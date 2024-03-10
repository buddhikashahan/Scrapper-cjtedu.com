import requests
res = requests.get('https://cjtedu.com')
print(res.text)  # Print the HTML content
print(res.status_code)  # Print the status code
