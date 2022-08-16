import subprocess

# shell=True will allows "ls -l" to be used, if not set then we need to use ["ls","-la"]
subprocess.run("ls -l",shell=True)
#####OUTPUT####
# total 4
# -rw-rw-r-- 1 guru guru 616 Aug 16 09:59 python_subprocess.py
################

#Capture output to variable res
res = subprocess.run(["ls","-la"],capture_output=True)
print("The result of {} is : {} ".format(res.args,res.stdout))
#print("Decoded output -{} ".format(res.stdout.decode()))
#####OUTPUT####
#The result of ['ls', '-la'] is : b'total 20\ndrwxrwxr-x 4 guru guru 4096 Aug 16 10:01 .\ndrwxrwxr-x 3 guru guru 4096 Aug 16 09:47 ..\ndrwxrwxr-x 7 guru guru 4096 Aug 16 09:47 .git\ndrwxrwxr-x 3 guru guru 4096 Aug 16 09:58 .idea\n-rw-rw-r-- 1 guru guru  715 Aug 16 10:01 python_subprocess.py\n'
################

#To remove the encoded output
res = subprocess.run(["ls","-la"],capture_output=True,text=True)
print(res.stdout)


#output without exception
res = subprocess.run(["ls","-la","ddd"],capture_output=True,text=True)
print(res.stderr)
#output
#ls: cannot access 'ddd': No such file or directory

#output with exception
res = subprocess.run(["ls","-la","ddd"],capture_output=True,text=True,check=True)
print(res.stderr)
##OUTPUT#
#Traceback (most recent call last):
#   File "/home/guru/guru/quick_python/python_subprocess.py", line 30, in <module>
#     res = subprocess.run(["ls","-la","ddd"],capture_output=True,text=True,check=True)
#   File "/usr/lib/python3.8/subprocess.py", line 516, in run
#     raise CalledProcessError(retcode, process.args,
# subprocess.CalledProcessError: Command '['ls', '-la', 'ddd']' returned non-zero exit status 2.
