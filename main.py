import sys
import os

def path_join(file_name: str) -> str:
	return os.path.join(os.getcwd(), file_name)

if len(sys.argv) == 1 or \
	not os.path.exists(path_join(sys.argv[1])):
	print('File not given or nonexistent.')
	sys.exit()
code = sys.argv[1]
compiled = path_join(f'{code[:-2]}[compiled]')
if len(sys.argv) > 2:
	compiled = path_join(sys.argv[2])
os.system(f'gcc {code} -o {compiled} && {compiled}')
