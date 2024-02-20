import requests


def call_api(endpoint, token):
    headers = {"Authorization": token}
    response = requests.post(f"http://127.0.0.1:8000/{endpoint}/", headers=headers)
    return response
