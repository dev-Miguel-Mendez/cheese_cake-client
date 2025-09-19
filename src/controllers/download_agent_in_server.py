from lib.ssh_client import ssh_client



def download_agent_in_server():

    print("Downloading agent in server")

    ssh_client.exec_command('cd ~/')
    ssh_client.exec_command('mkdir cheese_cake')
    ssh_client.exec_command('cd cheese_cake')
    si, so, se = ssh_client.exec_command('ls -la')

    print(so.read().decode())