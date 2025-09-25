from lib.ssh_client import ssh_client
from colorama import Back, Fore
from utils.exec_paramiko_command_and_print import exec_paramiko_command_and_print



AGENT_REPOSITORY_DIR = f"~/Desktop/cheese_cake/cheese_cake_repository"
# CHEESE_CAKE_EXECUTABLE_URL = "https://github.com/dev-Miguel-Mendez/cheese_cake-agent/releases/download/my_tag/cheese_cake"
CHEESE_CAKE_REPO_URL = "https://github.com/dev-Miguel-Mendez/cheese_cake-agent.git"



def download_agent_in_server():

    ssh_client.exec_command(f'mkdir -p {AGENT_REPOSITORY_DIR}') #* If already exists, it won't throw an error

    #* Remove everything to always get the latest version. (Could try "git merge" instead)  and THEN CLONING

    exec_paramiko_command_and_print(
        cmd=f"rm -rf ./* ./.??* && git clone {CHEESE_CAKE_REPO_URL} .",
        cwd=AGENT_REPOSITORY_DIR
    )

    print(Back.GREEN + "Downloaded agent in server!" + Back.RESET)



def start_agent():
    si, so, se = ssh_client.exec_command(f'test -d {AGENT_REPOSITORY_DIR}/.git') #type: ignore # pylint: disable=all
    repo_exists = so.channel.recv_exit_status()

    if repo_exists == 1:
        raise Exception(Fore.RED + "Agent not downloaded!" + Fore.RESET)

    #% Even the server was installed and ran previously, all these commands can run again.

    exec_paramiko_command_and_print(cmd="python3 -m venv .venv", cwd=AGENT_REPOSITORY_DIR)

    exec_paramiko_command_and_print(cmd="source .venv/bin/activate && pip install -r requirements.txt", cwd=AGENT_REPOSITORY_DIR)
    
    exec_paramiko_command_and_print(cmd="source .venv/bin/activate && python3 -m agent.run_server", cwd=AGENT_REPOSITORY_DIR)
