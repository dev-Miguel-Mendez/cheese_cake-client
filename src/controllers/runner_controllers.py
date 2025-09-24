import os
import json
import requests


host = os.environ.get("HOST")
port = os.environ.get("HOST_AGENT_PORT")


#* Sending "runner-config.json" to agent.
def send_runner_config_file():
    with open("runner-config.json", "r") as f:
        runner_config_dict = json.load(f)
    data = requests.post(f'http://{host}:{port}/runner/set-config', json=runner_config_dict, timeout=5)
    print(data.json())



def download_and_start_runner():
    data = requests.post(f"http://{host}:{port}/runner/download-and-run", timeout=60)
    print(data.json())

