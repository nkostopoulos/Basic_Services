# slightly modified from https://stackoverflow.com/questions/8382847/how-to-ssh-connect-through-python-paramiko-with-ppk-public-key

import paramiko

ssh = paramiko.SSHClient()

hostname = 'xxxxx.netmode.ece.ntua.gr'
myUserName = 'yyyyy'
myKeyFilename = '/root/.ssh/id_rsa'

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname, username=myUserName, key_filename=myKeyFilename)

SAMPLING_N = 64

command = """ovs-vsctl -- --id=@sflow create sflow agent=ens18 target="192.168.1.203:6343" header=128 sampling=""" + str(SAMPLING_N) + """ polling=0 -- set bridge br0 sflow=@sflow"""

print(command)

stdin, stdout, stderr = ssh.exec_command(command)

print stdout.readlines()

ssh.close()
