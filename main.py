import sys
import os

def path_join(file_name: str) -> str:
	return os.path.join(os.getcwd(), file_name)


def main():
	if len(sys.argv) == 1 or \
		not os.path.exists(path_join(sys.argv[1])):
		print('File not given or nonexistent.')
		return
	code = sys.argv[1]
	compiled = path_join(f'{code[:-2]}__COMPILED')
	if len(sys.argv) > 2:
		compiled = path_join(sys.argv[2])
	os.system(f'g++ {code} -o {compiled}')
	if os.path.exists(path_join(compiled)):
		os.system(f'{compiled}')
	else:
		print("Compilation error.")
	if sys.argv[-1] != '-p':
		os.remove(compiled)


if __name__ == "__main__":
	main()
