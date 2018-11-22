import os, sys
import time

def main():
	# if 3, 1 args
	command_len = len(sys.argv)
	command = sys.argv[1]
	result = "null"
	cd_str = ""
	if command == "o":
		command_obj_1 = sys.argv[2]
		current_location = os.popen("a=`cd " + command_obj_1 + ";pwd;`;echo $a;").readlines()[0]
		current_location = current_location.replace("\n", "")
		#TODO: 生成的命令记录文件 修改为自己的目录
		with open('/home/disk1/shicuiliang/tool/python/command_execute/command.rpc', 'w') as file:
			file.write("open " + current_location.encode('utf-8'))
	elif command == "sub":
		command_obj_1 = sys.argv[2]
		current_location = os.popen("a=`cd " + command_obj_1 + ";pwd;`;echo $a;").readlines()[0]
		current_location = current_location.replace("\n", "")
		#TODO: 生成的命令记录文件 修改为自己的目录
		with open('/home/disk1/shicuiliang/tool/python/command_execute/command.rpc', 'w') as file:
			file.write("sub " + current_location.encode('utf-8'))
	elif command == "make":
		result = os.popen("cd .;bash moduleMake userdebug mmm vendor/mediatek/proprietary/packages/apps/MtkSettings").readlines()
		for i in result:
			print i,
	elif command == "git":
		for x in xrange(1,8):
			try:
				result = os.popen(cd_str + 'ls -a | grep ".git"').readlines()[0].replace("\n", "")
			except Exception as e:
				cd_str += "cd ..;"
				# print "haven't .git file"
			if result == ".git":
				git_folder = os.popen(cd_str+'pwd').readlines()[0].replace("\n", "")
				print git_folder + " has .git file"
				shell = "cp /home/st/.git/hooks/commit-msg " + git_folder + "/.git/hooks/"
				# print shell
				print os.popen(shell)
				break
	elif command == "bird.mk":
		current_folder = os.popen("pwd").readlines()[0].replace("\n", "")
		cd_str = "cd device/mediatek/mt6739;"
		try:
			git_branch = os.popen(cd_str + 'git branch|grep "*"').readlines()[0].replace("\n", "").replace("* ", "")
			print git_branch
		except Exception as e:
			print os.popen(cd_str + 'git checkout master').readlines()
			git_branch = os.popen(cd_str + 'git branch|grep "*"').readlines()[0].replace("\n", "").replace("* ", "")
			print git_branch
		print os.popen(cd_str + "git pull origin " + git_branch).readlines()
		
		current_day = time.strftime("%Y-%m-%d", time.localtime())
		bug = sys.argv[2]
		bird_define = sys.argv[3]
		bird_prop = sys.argv[4]
		# f bird.mk 命令 如果需要 修改为自己邮箱
		bird_mk_add = "#@ {bird: For fix bug#" + bug + ", add by shicuiliang@szba-mobile.com " + current_day + ".\nifeq ($(strip $(" + bird_define +")), yes)\n\tPRODUCT_PROPERTY_OVERRIDES += " + bird_prop +" = true\nendif\n#@ }"
		print bird_mk_add

		file = current_folder + '/device/mediatek/mt6739/bird.mk'
		with open(file, 'a+') as f:
			f.write("\n\n" + bird_mk_add + '\n')

		print os.popen(cd_str + 'git diff').readlines()[1]
	elif command == "note":
		modify_file = os.popen('git status -s|grep "M"').readlines()
		print modify_file
		modify_file_count = int(os.popen('git status -s|grep "M"|wc -l').readlines()[0].replace("\n", ""))
		for x in xrange(0, modify_file_count):
			shell = 'git diff ' + modify_file[x].replace("\n", "").replace(" M ", "")
			print shell
			print os.popen(shell).readlines()
	elif command == "cpu":
		cpu_lists = os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head').readlines()
		for i in cpu_lists:
			print i,
	elif command == "mem":
		mem_lists = os.popen('ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head').readlines()
		for i in mem_lists:
			print i,
	else:
		print "test hello"

if __name__ == '__main__':
	main()
