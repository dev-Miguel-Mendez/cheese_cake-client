import os
import json
import requests

host = os.environ.get("HOST")
port = os.environ.get("HOST_AGENT_PORT")


#% These requests will only work when agent is on port <HOST_AGENT_PORT>.

#* Sending "runner-config.json" to agent.
def send_runner_config_file():
    with open("runner-config.json", "r") as f:
        runner_config_dict = json.load(f)
    
    try:
        response = requests.post(f'http://{host}:{port}/runner/set-config', json=runner_config_dict, timeout=5)
        response.raise_for_status() #* If the status code is 400 or higher (client or server error), it raises a requests.exceptions.HTTPError.
        print(response.json())
    except requests.exceptions.HTTPError as e:
        print(e.response.text)



def download_and_start_github_runner():
    try:
        response = requests.post(f"http://{host}:{port}/runner/download-and-run", timeout=60)
        response.raise_for_status() #* If the status code is 400 or higher (client or server error), it raises a requests.exceptions.HTTPError.
        print(response.json())
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
