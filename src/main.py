from typing import Dict, Callable, Any
import subprocess
import questionary
import bootstrap_env # pylint: disable=all #type: ignore
from controllers.download_agent_in_server import download_agent_in_server
from controllers.runner_controllers import send_runner_config_file

# servers = {
#     "US": "123",
#     "EUR": "456"
# } #! I GUESS YOU WILL JUST MANAGE A SINGLE  PROJECT.

# actions = {
#     "SPAWN": "Spawn more containers",
#     "REMOVE:": "Remove existing containers"
    # "Spawn EC2 instance": "",
    # "Shut down EC2 instance": "",
    # "Set CI/CD for instance": ""
# }


subprocess.run("clear")

actions: Dict[str, Callable [[], Any]] = {
    "Download agent in server": download_agent_in_server,
    "Send runner configuration file": send_runner_config_file,
    "Spawn more containers": lambda: print('Test'),
    "Remove existing containers": lambda: (print('Test'), print("YOU CAN DO MANY THINGS IN A LAMBDA")),
    "Spawn EC2 instance": lambda: print(''),
    "Shut down EC2 instance": lambda: print(""),
    "Set CI/CD for instance": lambda: print(""),

    "Exit": lambda: exit(0),
}



#% If you want to use this program with a different project you may want to pick a different configuration file.

result = questionary.prompt([
    {
        "type": "select",
        "name": "action",
        "message": "Select an instance to connect to:",  #% An instance and not a "project" because you will usually only handle a single project.
        "choices": list(actions.keys())
    }
])

actions[result["action"]]()

