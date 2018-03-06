# coding:utf-8
# Demo1: using fork just useful for Linux
import os
if __name__ == '__main__':
	print 'current Process (%s) start ...' %(os.getpid())
	pid = os.fork()
	if pid < 0:
		print 'error in fork'
	elif pid == 0:
		print 'I an child process(%s) and my parent process is (%s)',(os.getpid(),os.getppid())
	else:
		print 'I(%s) created a child process (%s).',(os.getpid(),pid)

# Demo2:using multiprocessing module for crate multiprocess.(It's useful for Linux and Windows)
import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
	print 'Child process %s (%s) Running...' % (name,os.getpid())

if __name__ == '__main__':
	print 'Parent process %s.' % os.getpid()
	for i in range(5):
		p = Process(target=run_proc,args=(str(i),))
		print 'Process will start.'
		p.start()
	p.join()
	print 'Process end.'