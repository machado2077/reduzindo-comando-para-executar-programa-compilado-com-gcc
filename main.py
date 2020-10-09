import sys
import os

code = sys.argv[1]
compiled = f'{code[:-2]}_compiled'
if sys.argv[2]:
	compiled = sys.argv[2]
os.system(f'gcc {code} -o {compiled} && ./{compiled}')
