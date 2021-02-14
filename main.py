"""
expected command:

$ alias file_name [compiled_name] [permanent_compiled_file]
"""

import sys
import os


def path_join(file_name: str) -> str:
	return os.path.join(os.getcwd(), file_name)


def main():
	if len(sys.argv) == 1 or \
		not os.path.exists(path_join(sys.argv[1])):
		print('File not given or nonexistent.')
		return
	file_name = sys.argv[1]

	if file_name.endswith('.c'):
		compiled = path_join(f'{file_name[:-2]}__COMPILED')
		driver = 'gcc'
	elif file_name.endswith('.cpp'):
		compiled = path_join(f'{file_name[:-4]}__COMPILED')
		driver = 'g++'
	else:
		print("Unknown source code extension.")
		return
	
	if len(sys.argv) >= 3:
		compiled = path_join(sys.argv[2])
	os.system(f'{driver} {file_name} -o {compiled}')
	
	if os.path.exists(path_join(compiled)):
		os.system(f'{compiled}')
	else:
		return
	
	if not '-p' in sys.argv:
		os.remove(compiled)


if __name__ == "__main__":
	main()
