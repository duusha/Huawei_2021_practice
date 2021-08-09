import time
from distutils.compiler import new_compiler
compiler = new_compiler()

start_time = time.time()

compiler.compile(['test.c'])
compiler.link_executable(['test.o'], 'test')

print("---%s seconds ---" % (time.time()-start_time))