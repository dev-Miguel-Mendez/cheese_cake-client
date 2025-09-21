import os
import requests
import json

with open("runner-config.json", "r") as f:
    runner_config_dict = json.load(f)


server_host = os.environ.get("HOST")

def send_runner_config_file():
    requests.post(f'{server_host}/', json=runner_config_dict)