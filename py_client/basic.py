import requests


endpoint = "https://github.com/"

get_response = requests.get(endpoint)


print(get_response.text)


