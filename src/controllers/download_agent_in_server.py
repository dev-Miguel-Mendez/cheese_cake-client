from lib.ssh_client import ssh_client
from colorama import Back



WORK_DIR = "~/Desktop/cheese_cake"

def download_agent_in_server():
    """ Create Desktop/cheese_cake and cd into it """

    ssh_client.exec_command(f'mkdir -p {WORK_DIR}')


    si, so, se = ssh_client.exec_command(f'test -f {WORK_DIR}/cheese_cake_executable') #type: ignore # pylint: disable=all

    return_code = so.channel.recv_exit_status()

    print(return_code)


    print(Back.GREEN + "Downloaded agent in server!" + Back.RESET)