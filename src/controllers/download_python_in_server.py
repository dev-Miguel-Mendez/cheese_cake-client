from lib.ssh_client import ssh_client
from colorama import Fore
def install_python_on_server():
    si, so, se = python_exist = ssh_client.exec_command("which python3") #type: ignore # pylint: disable=all

    return_code = so.channel.recv_exit_status()

    if(return_code == 0):
        raise Exception(Fore.RED + "Python3 already installed" + Fore.RESET)
    
    ssh_client.exec_command("apt update")
    ssh_client.exec_command("apt install -y  python3 python3-pip python3-venv")

    si, so, se = python_exist = ssh_client.exec_command("which python3") #type: ignore # pylint: disable=all
    
    if(return_code == 1):
        raise Exception(Fore.RED + "Python3 not present after installation" + Fore.RESET)
    
    print("Success")