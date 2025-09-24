from lib.ssh_client import ssh_client
from colorama import Back, Fore


WORK_DIR = "~/Desktop/cheese_cake"
AGENT_REPOSITORY_DIR = f"{WORK_DIR}/cheese_cake_repository"
# CHEESE_CAKE_EXECUTABLE_URL = "https://github.com/dev-Miguel-Mendez/cheese_cake-agent/releases/download/my_tag/cheese_cake"
CHEESE_CAKE_REPO_URL = "https://github.com/dev-Miguel-Mendez/cheese_cake-agent.git"



def check_repo_exists() -> int:
    si, so, se = ssh_client.exec_command(f'test -d {AGENT_REPOSITORY_DIR}/.git') #type: ignore # pylint: disable=all
    return so.channel.recv_exit_status()



def download_agent_in_server():

    ssh_client.exec_command(f'mkdir -p {WORK_DIR}') #* If already exists, it won't throw an error

    ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && rm -rf ./* ./.??* && git clone {CHEESE_CAKE_REPO_URL} .") #* Remove everything to always get the latest version. (Could try "git merge" instead) 
    print(Back.GREEN + "Downloaded agent in server!" + Back.RESET)



def start_agent():
    si, so, se = ssh_client.exec_command(f'test -d {AGENT_REPOSITORY_DIR}/.git') #type: ignore # pylint: disable=all
    repo_exists = so.channel.recv_exit_status()

    if repo_exists == 1:
        raise Exception(Fore.RED + "Agent not downloaded!" + Fore.RESET)

    #$ Need to run cd multiple times because exec_command opens  a new shell every time. 

    si, so, se = ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && python3 -m venv .venv") #type: ignore # pylint: disable=all

    print(so.read().decode())
    print(se.read().decode())

    si, so, se = ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && source .venv/bin/activate && pip install -r requirements.txt") #type: ignore # pylint: disable=all

    print(so.read().decode())
    print(so.read().decode())

    si, so, se = ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && source .venv/bin/activate && python3 -m agent.run_server") #type: ignore # pylint: disable=all
    print(so.read().decode())
    print(se.read().decode())