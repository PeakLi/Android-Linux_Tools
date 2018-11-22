#coding=utf-8
import os
import socket
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys_cmd_path = "C:\\Windows\\System32"
# TODO 1. sublime 修改为自己sublime的地址
location_windows_sublime = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"

flash_tool_path = "E:\\Cuiliang.shi\\tools\\SP_Flash_Tool_exe_Windows_v5.1736.00.000\\flash_tool.exe"
studio_path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
xshell_path = "C:\\Program Files (x86)\\NetSarang\\Xshell 5\\Xshell.exe"


# TODO 2. 修改为自己服务器的IP
location_server = "\\\\192.168.149.172\\"

def handle_folder(operate, path):
    if path.index("/home/disk1/") > -1:
        path = path.replace("/home/disk1/", "Disk1/")
    path = path.replace("/", "\\")
    path = location_server + path
    try:
        if operate == "sub":
            print "sub: " + path
            result = os.popen('"'+ location_windows_sublime +'" '+ path).readlines()
        elif operate == "open":
            print "open: " + path
            result = os.popen('start '+ path).readlines()[0]
    except Exception as e:
        result = str(e)
    return result

def handle_adb(operate, path):
    if path.index("/home/disk1/") > -1:
        # TODO 3. 服务器下 /home/disk1/  对应 windows共享目录下的 \\1922.xxxx\Disk1\
        path = path.replace("/home/disk1/", "Disk1/")
    path = path.replace("/", "\\")
    path = location_server + path
    try:
        result = os.popen('start '+ path).readlines()[0]
    except Exception as e:
        result = str(e)
    return result


if __name__ == '__main__':
    # TODO 4. 修改为自己windows电脑的IP
    address = ('192.168.149.134', 6789)
    max_size = 1000

    print('Start server at {}'.format(datetime.now()))
    print('Waiting for a client now !')

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)
    client,addr = server.accept()
    result = 0

    while True:
        buf = client.recv(max_size)
        if buf != 'continue':
            print "get command: " + buf
            command_arguments = buf.split(" ")
            if command_arguments[0] == "open" or command_arguments[0] == "sub":
                result = handle_folder(command_arguments[0], command_arguments[1])
            elif command_arguments[0] == "adb":
                result = handle_adb(command_arguments[0], command_arguments[1])
        client.send(str(result))

    client.close()
    server.close()
