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

    repo_exists = check_repo_exists()

    if repo_exists == 0:
        raise Exception(Fore.RED + "Agent already downloaded" + Fore.RESET)
    # ssh_client.exec_command(f"curl -L -o {WORK_DIR}/cheese_cake_executable {CHEESE_CAKE_EXECUTABLE_URL}")
    ssh_client.exec_command(f"git clone {CHEESE_CAKE_REPO_URL} {AGENT_REPOSITORY_DIR}")
    print(Back.GREEN + "Downloaded agent in server!" + Back.RESET)



def start_agent():
    repo_exists = check_repo_exists()

    if repo_exists == 1:
        raise Exception(Fore.RED + "Agent not downloaded!" + Fore.RESET)
    

    ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && python3 -m venv .venv")

    ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && source .venv/bin/activate && pip install -r requirements.txt")

    ssh_client.exec_command(f"cd {AGENT_REPOSITORY_DIR} && source .venv/bin/activate && python3 -m agent.run_server.py")