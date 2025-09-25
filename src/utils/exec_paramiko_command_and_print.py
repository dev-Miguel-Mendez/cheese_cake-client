from lib.ssh_client import ssh_client

#% This is simply a helper function to avoid duplication of:
#  "print(stdout.read().decode())" 
#  "print(stderr.read().decode())"

def exec_paramiko_command_and_print(cmd: str, cwd: str | None =None):
    if cwd:
        cmd = f"cd {cwd} && {cmd}"
    
    stdin, stdout, stderr = ssh_client.exec_command(cmd) #type: ignore # pylint: disable=all

    print(stdout.read().decode())
    print(stderr.read().decode())

    #* Returns (return_code, stdout, stderr)
    return stdout.channel.recv_exit_status(), stdout, stderr