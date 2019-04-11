# slightly modified from https://stackoverflow.com/questions/8382847/how-to-ssh-connect-through-python-paramiko-with-ppk-public-key

import paramiko

ssh = paramiko.SSHClient()


hostname = 'xxxxxx.netmode.ece.ntua.gr'
myUserName = 'yyyyy'
myKeyFilename = 'PRIVATE_KEY_PATH'

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname, username=myUserName, key_filename=myKeyFilename)

stdin, stdout, stderr = ssh.exec_command('touch hello.txt')

print stdout.readlines()

ssh.close()
