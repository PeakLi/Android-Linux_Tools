import socket
import time
import socket
from datetime import datetime

if __name__ == '__main__':
	# TODO: 修改为windows电脑的IP
	address = ('192.168.149.134',6789)
	max_size =1000
	print("Start the client at {}".format(datetime.now()))
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(address)

	flag = '1'
	old_command = "hello"

	while True:
		time.sleep(1)
		file = open('command.rpc', 'r')
		command = file.read().decode('utf-8')
		file.close()
		if old_command == command:
			client.sendall("continue".encode("utf-8"))
			data = client.recv(max_size)
			continue
		else:
			print("command execute: " + command)
			command_arguments = command.split(" ")

			client.sendall(command.encode("utf-8"))
			data = client.recv(max_size)
			print(format(datetime.now()), "replay: " , data)
		old_command = command

	client.close()
