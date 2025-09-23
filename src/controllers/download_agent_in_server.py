from lib.ssh_client import ssh_client
from colorama import Back, Fore


WORK_DIR = "~/Desktop/cheese_cake"
CHEESE_CAKE_EXECUTABLE_URL = "https://github.com/dev-Miguel-Mendez/cheese_cake-agent/releases/download/my_tag/cheese_cake"

def download_agent_in_server():

    ssh_client.exec_command(f'mkdir -p {WORK_DIR}')

    si, so, se = ssh_client.exec_command(f'test -f {WORK_DIR}/cheese_cake_executable') #type: ignore # pylint: disable=all

    return_code = so.channel.recv_exit_status()

    if return_code == 0:
        raise Exception(Fore.RED + "Agent already downloaded" + Fore.RESET)
    ssh_client.exec_command(f"curl -L -o {WORK_DIR}/cheese_cake_executable {CHEESE_CAKE_EXECUTABLE_URL}")

    print(Back.GREEN + "Downloaded agent in server!" + Back.RESET)