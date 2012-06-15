import tkFileDialog
import subprocess
import os,sys,resource,syslog,time,signal
import compare_outfiles
import datetime
import nocalls
from sdust_oj import settings
STD_MB = 1048576
DEBUG = 0
PROBLEMDIR = 'problems'
TIME_LIMIT = 200
FILE_LIMIT = (STD_MB << 5)
MEMORY_LIMIT = (STD_MB << 7)
p = None

from sdust_oj import status as STATUS

OJ_WT0=STATUS.pending #Waiting0(Pending)?
OJ_WT1=1 #Waiting1(Pending & Restarting)?
OJ_CI=STATUS.compiling  #Compiling..
OJ_RI=3  #Running & Judging..
OJ_AC=STATUS.output_check_ok  #Accepted
OJ_PE=STATUS.presentation_error  #Presentation Error
OJ_WA=STATUS.wrong_answer  #Wrong Answer
OJ_TL=7  #Time Limit Exceed
OJ_ML=8  #Memory Limit Exceed
OJ_OL=9  #Output Limit Exceed
OJ_RE=STATUS.runtime_error #Runtime Error
OJ_CE=STATUS.compiled_error #Compile Error
OJ_CO=12 #??

useful_types = ['c','cc','pas','java','rb','sh','py','php','pl','cs']

def debug(msg):
	print msg
	syslog.syslog(msg)

#submission: id,problem_id,status,sub_time,used_memory,used_time,user_id,code_type,code
def get_current_status(sub_time,mm,tt,file_type,code_length,cur_status):
	#store the used datas into mysql or use other methods
	print str(sub_time)+';'+str(mm)+';'+str(tt)+';'+file_type+';'+str(code_length)+';'+str(cur_status)
	pass
class crun_interface:
	CP_Command = []
	Run_Command = []
	def __init__(self):
		pass

class crun_C(crun_interface):
	def __init__(self,file_name='Main.c'):
        	CP_C = [ "gcc", file_name, "-o", "Main", "-Wall", "-lm",
			"--static", "-std=c99", "-Werror=implicit-function-declaration", "-DONLINE_JUDGE"]
		Run_C = './Main'
		self.CP_Command = CP_C
		self.Run_Command = Run_C

class crun_X(crun_interface):
	def __init__(self,file_name='Main.cc'):
        	CP_X = [ "g++", file_name, "-o", "Main", "-Wall",
			"-lm", "--static", "-DONLINE_JUDGE"]
		Run_CC = './Main'
		self.CP_Command = CP_X
		self.Run_Command = Run_CC

class crun_P(crun_interface):
	def __init__(self,file_name='Main.pas'):
        	CP_P = [ "fpc", file_name, "-O2","-Co", "-Ct","-Ci"]
		Run_P = './Main'
		self.CP_Command = CP_P
		self.Run_Command = Run_P

class crun_J(crun_interface):
	def __init__(self,file_name='Main.java'):
        	CP_J = [ "javac", "-J-Xms32m", "-J-Xmx256m", file_name]
		#file = sourcefile.split('.')[0]   ??
		Run_J = ['java',file_name.split('.')[0]]
		self.CP_Command = CP_J
		self.Run_Command = Run_J

class crun_R(crun_interface):
	def __init__(self,file_name='Main.rb'):
		CP_R = [ "ruby", "-c", file_name]
		Run_R = ['ruby',file_name]
		self.CP_Command = CP_R
		self.Run_Command = Run_R

class crun_B(crun_interface):
	def __init__(self,file_name='Main.sh'):
        	CP_B = [ "chmod", "+rx", file_name]
		Run_B = ['bash',file_name]
		self.CP_Command = CP_B
		self.Run_Command = Run_B

class crun_Y(crun_interface):
	def __init__(self,file_name='Main.py'):
        	CP_Y = [ "python","-c","import py_crun; py_crun.crun(r'%s')"%(file_name)]
		Run_Y = ['python',file_name]
		self.CP_Command = CP_Y
		self.Run_Command = Run_Y

class crun_PH(crun_interface):
	def __init__(self,file_name='Main.php'):
	        CP_PH = [ "php", "-l",file_name]
		Run_PH = ['php','-f',file_name]
		self.CP_Command = CP_PH
		self.Run_Command = Run_PH

class crun_PL(crun_interface):
	def __init__(self,file_name='Main.pl'):
	        CP_PL = [ "perl","-c", file_name]
		Run_PL = ['perl',file_name]
		self.CP_Command = CP_PL
		self.Run_Command = Run_PL

class crun_CS(crun_interface):
	def __init__(self,file_name='Main.cs'):
	        CP_CS = [ "gmcs","-warn:0", file_name]
		file = file_name.split('.')[0]
		Run_CS = ['mono',file+'.exe']
		self.CP_Command = CP_CS
		self.Run_Command = Run_CS


def search_dir(problem_dir):
	std_io_list = []
	for root,dirs,files in os.walk(problem_dir):
		for fn in files:
			if fn.endswith('.in') and os.path.exists(root+'/'+fn[0]+'.out'):
				a = (root+'/'+fn,root+'/'+fn[0]+'.out')
				std_io_list.append(a)
	return std_io_list

def testcode(s):
	s=s.replace('\n','')
	s=s.replace('','')
	s=s.replace('\r','')
	for nocall in nocalls.nocalls:
		if s.find(nocall+'(')>=0:
			return False
	return True

def compile(file_name):
	os.chdir(os.path.dirname(file_name))
	file_type = file_name.split('.')[-1]
	pid = os.fork()
        status = 0
	if pid == 0:
        	resource.setrlimit(resource.RLIMIT_CPU,(60,60))
        	resource.setrlimit(resource.RLIMIT_FSIZE,(80 * STD_MB,80 * STD_MB))
        	resource.setrlimit(resource.RLIMIT_AS, (1024 * STD_MB,1024 * STD_MB))
        	if file_type != 'pascal':#lang!=2
			sys.stderr = open('ce.txt','w+')
		        #redirect
        	else:
	    		sys.stdout = open('ce.txt','w+')
		code_length = os.path.getsize(file_name)
		print 'code_length:'+str(code_length)+'B'
		mm = 0
		tt = 0#init the data & used to store the current status
		sub_time = datetime.datetime.now()
		
		#check the source code
		f = file(file_name,'r')
		source = f.read() 
		if testcode(source) == False:
			status = OJ_RE
			get_current_status(sub_time,mm,tt,file_type,code_length,status)
			sys.exit(OJ_RE)  
		f.close()
		
		if file_type in useful_types:
			a = {
				'c':lambda:crun_C(file_name),
		    		'cc':lambda:crun_X(file_name),
				'pas':lambda:crun_P(file_name),
				'java':lambda:crun_J(file_name),
				'rb':lambda:crun_R(file_name),
				'sh':lambda:crun_B(file_name),
				'py':lambda:crun_Y(file_name),
				'php':lambda:crun_PH(file_name),
				'pl':lambda:crun_PL(file_name),
				'cs':lambda:crun_CS(file_name)
			}[file_type]()
		else:
	    		debug('Type not exist '+'Compile Error')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CE)
			sys.exit(OJ_CE)
		debug('Compiling...')
		get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CI)
		if subprocess.call(a.CP_Command) != 0:
			status = OJ_CE
			debug('Compile Error')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CE)
		else:
			status = STATUS.compile_ok
			debug("Compile OK")
        	if DEBUG:
	    		print 'compile end\n' 

	else:
        	os.waitpid(pid, 0)
		if DEBUG:
	    		print 'status=%d'%status
	return status
def compile_run(file_name,problem):
	file_type = file_name.split('.')[-1]
	pid = os.fork()
	if pid == 0:
        	resource.setrlimit(resource.RLIMIT_CPU,(60,60))
        	resource.setrlimit(resource.RLIMIT_FSIZE,(80 * STD_MB,80 * STD_MB))
        	resource.setrlimit(resource.RLIMIT_AS, (1024 * STD_MB,1024 * STD_MB))
        	if file_type != 'pascal':#lang!=2
			sys.stderr = open('ce.txt','w+')
		        #redirect
        	else:
	    		sys.stdout = open('ce.txt','w+')
		code_length = os.path.getsize(file_name)
		print 'code_length:'+str(code_length)+'B'
		mm = 0
		tt = 0 #init the data & used to store the current status
		sub_time = datetime.datetime.now()
		
		#check the source code
		f = file(file_name,'r')
		source = f.read() 
		if testcode(source) == False:
			status = OJ_RE
			get_current_status(sub_time,mm,tt,file_type,code_length,status)
			sys.exit(OJ_RE)  
		f.close()
		
		if file_type in useful_types:
			a = {
				'c':lambda:crun_C(file_name),
		    		'cc':lambda:crun_X(file_name),
				'pas':lambda:crun_P(file_name),
				'java':lambda:crun_J(file_name),
				'rb':lambda:crun_R(file_name),
				'sh':lambda:crun_B(file_name),
				'py':lambda:crun_Y(file_name),
				'php':lambda:crun_PH(file_name),
				'pl':lambda:crun_PL(file_name),
				'cs':lambda:crun_CS(file_name)
			}[file_type]()
		else:
	    		debug('Type not exist '+'Compile Error')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CE)
			sys.exit(OJ_CE)
		debug('Compiling...')
		get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CI)
		if subprocess.call(a.CP_Command):
			debug('Compile Error')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_CE)
			sys.exit(OJ_CE)
        	if DEBUG:
	    		print 'compile end\n' 
		#######follow is the part of run
		problem_dir = PROBLEMDIR + '/' + str(problem)
		std_io_list = search_dir(problem_dir)
		print 'start run-----'
		for std_io in std_io_list:
			print 'one run start'
			run(std_io,problem,mm,tt,file_type,code_length,a,sub_time)
			print 'one run over'
		status = OJ_AC
		get_current_status(sub_time,mm,tt,file_type,code_length,status)
		sys.exit(OJ_AC)
	else:
		status = 0
        	os.waitpid(pid,status)
		if DEBUG:
	    		print 'status=%d'%status
		return status

def output_check_main(meta_id, io_list, sid):
	status = STATUS.output_check_ok
	for io_id in io_list:
		std_io = os.path.join(settings.ROOT_PATH, "judge_root", "data",
				str(meta_id), "testdata", str(io_id)+".out")
		real_io = os.path.join(settings.ROOT_PATH, "judge_root", "work", sid, str(io_id)+".real_out")
		status = compare_outfiles.compare(real_io, std_io)
		if status in [OJ_PE, OJ_WA, OJ_RE]:
			return status
	return status

import shutil
def run_main(meta_id, io_list, sid, file_name):
	status = STATUS.run_ok
	mm = tt = 0
	file_type = file_name.split('.')[-1]
	if file_type in useful_types:
		a = {
			'c':lambda:crun_C(file_name),
	    		'cc':lambda:crun_X(file_name),
			'pas':lambda:crun_P(file_name),
			'java':lambda:crun_J(file_name),
			'rb':lambda:crun_R(file_name),
			'sh':lambda:crun_B(file_name),
			'py':lambda:crun_Y(file_name),
			'php':lambda:crun_PH(file_name),
			'pl':lambda:crun_PL(file_name),
			'cs':lambda:crun_CS(file_name)
		}[file_type]()
	else:
		debug('Type not exist '+'Compile Error')
		status = OJ_CE
	for io_id in io_list:
		src_io = os.path.join(settings.ROOT_PATH, "judge_root", "data",
				str(meta_id), "testdata", str(io_id)+".in")
		dst = os.path.join(settings.ROOT_PATH, "judge_root", "work", sid)
		shutil.copy2(src_io, dst)
		std_io = os.path.join(dst, str(io_id)+".in")
		status, m, t = run(std_io, a, io_id)
		if status in [OJ_ML, OJ_TL, OJ_RE, OJ_OL]:
			return status, mm, tt
		mm += m
		tt += t
	return status, mm, tt 
	
def run(std_io, a, io_id):
	mm = 0
	tt = 0
	status = STATUS.run_ok
	debug('Running...')
	start = time.time()
	print 'start'
	real_out = std_io.replace('.in','.real_out')
	p = subprocess.Popen(a.Run_Command,stdin=open(std_io,'r'),stdout=open(real_out,'w'))
	print 'after p'
	while p.poll() == None:
		s = file('/proc/'+str(p.pid)+'/status','r').read()
		if s.find('RSS')<0:
			continue
		s = s[s.find('RSS')+6:]
		s = s[s.find('KB')-1]
		mm = int(s)
		if mm > MEMORY_LIMIT:
			p.kill()
			debug('Memory Limit Exceed')
			status = OJ_ML
			break
		tt = int((time.time()-start)*1000)
		if tt > TIME_LIMIT:
			p.kill()
			debug('Time Limit Exceed')
			status = OJ_TL
			break

	print 'time cost:'+str(tt)+'ms'
	print 'memory cost:'+str(mm)+'kb'
	r = p.returncode
	debug('Exist status : %d'%r)
	if r!=0:
		debug('Run Error')
		status = OJ_RE
	len_outfile = os.path.getsize(real_out)
	if len_outfile >= FILE_LIMIT:
		debug('Output Limit Exceed')
		status = OJ_OL
	
	return status, mm, tt		
		
		
def run_copy(std_io,problem,mm,tt,file_type,code_length,a,sub_time):
	debug('Running...')
	get_current_status(sub_time,mm,tt,file_type,code_length,OJ_RI)
	if file_type == 'Java':
		a = 3
	start = time.time()
	print 'start'
	real_out = std_io[0].replace('.in','.real_out')
	p = subprocess.Popen(a.Run_Command,stdin=open(std_io[0],'r'),stdout=open(real_out,'w'))
	print 'after p '
	while p.poll() == None:
		s = file('/proc/'+str(p.pid)+'/status','r').read()
		if s.find('RSS')<0:
			continue
		s = s[s.find('RSS')+6:]
		s = s[s.find('KB')-1]
		mm = int(s)
		if mm > MEMORY_LIMIT:
			p.kill()
			debug('Memory Limit Exceed')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_ML)
			sys.exit(OJ_ML)
		tt = int((time.time()-start)*1000)
		if tt > TIME_LIMIT:
			p.kill()
			debug('Time Limit Exceed')
			get_current_status(sub_time,mm,tt,file_type,code_length,OJ_TL)
			sys.exit(OJ_TL)

	print 'time cost:'+str(tt)+'ms'
	print 'memory cost:'+str(mm)+'kb'
	r = p.returncode
	debug('Exist status : %d'%r)
	if r!=0:
		debug('Run Error')
		get_current_status(sub_time,mm,tt,file_type,code_length,OJ_RE)
		sys.exit(OJ_RE)
	len_outfile = os.path.getsize(real_out)
	if len_outfile >= FILE_LIMIT:
		debug('Output Limit Exceed')
		get_current_status(sub_time,mm,tt,file_type,code_length,OJ_OL)
		sys.exit(OJ_OL)
	result=compare_outfiles.compare(real_out,std_io[1])
	print 'After compare, one result :'+str(result)
	if result != OJ_AC:
		get_current_status(sub_time,mm,tt,file_type,code_length,result)
		sys.exit(result)
	
if __name__=="__main__":
        #file_name=tkFileDialog.askopenfilename()
	file_name = input('Input the file name:')
	problem = input('Input the problem_id:')
        compile_run(file_name,problem)
