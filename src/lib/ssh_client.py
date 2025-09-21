import os
import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh_client.connect(
    hostname=str(os.environ.get("HOST")), 
    username="root", 
    key_filename="/home/dwati/.ssh/hetzner", 
    passphrase=os.environ.get("SSH_PASSPHRASE")
)