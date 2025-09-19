import questionary
import bootstrap_env # pylint: disable=all #type: ignore
from controllers.download_agent_in_server import download_agent_in_server


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


#% If you want to use this program with a different project you may want to pick a different configuration file.

result = questionary.prompt([
    {
        "type": "select",
        "name": "Action",
        "message": "Select an instance to connect to:",  #% An instance and not a "project" because you will usually only handle a single project.
        "choices": ["Download agent in server", "Spawn more containers", "Remove existing containers", "Spawn EC2 instance", "Shut down EC2 instance", "Set CI/CD for instance"]
        # "choices":  list(actions.keys())
    }
])



match result["Action"]:

    case "Download agent in server":
        download_agent_in_server()

    case "Set CI/CD for instance":
        pass

    case _:
        print('')


