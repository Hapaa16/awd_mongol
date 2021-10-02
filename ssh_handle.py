from SSHLibrary import SSHLibrary
def ssh_handler(ip, user, password, command, port):
    print ("Executing command " + command + " on host " + ip)
    lib = SSHLibrary()
    lib.open_connection(ip, port=port)
    lib.login(username=user,password=password)   
    result = lib.execute_command(command)
    lib.close_connection()
    return result
