import json
import requests

with open("runner-config.json", "r") as f:
    runner_config_dict = json.load(f)

#* Sending "runner-config.json" to agent.

def send_runner_config_file():
    data = requests.post('http://localhost:3001/runner/set-config', json=runner_config_dict, timeout=5)
    print(data.json())


def download_and_start_runner():

    data = requests.post("http://localhost:3001/runner/download-and-run")

    print(data.json())

