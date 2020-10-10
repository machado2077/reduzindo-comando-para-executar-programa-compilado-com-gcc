import sys
import os

if len(sys.argv) == 1 or \
	not os.path.exists(os.path.join(os.getcwd(), sys.argv[1])):
	print('File not given or nonexistent.')
	sys.exit()
code = sys.argv[1]
compiled = f'{code[:-2]}[compiled]'
if len(sys.argv) > 2:
	compiled = sys.argv[2]
os.system(f'gcc {code} -o {compiled} && {compiled}')
