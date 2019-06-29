import paramiko

def sshCommand(hostname, port, username, password, command):
    f = paramiko.SSHClient()
    f.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f.load_system_host_keys()
    f.connect(hostname, port, username, password)#pkey=None, key_filename="/home/user/.ssh/mykey.pem")
    stdin, stdout, stderr = f.exec_command(command)
    print(stdout.read())
    stdout.channel.recv_exit_status()

    #lines = stdout_.readlines()
    #for line in lines:
    #    print (line)

    f.close()