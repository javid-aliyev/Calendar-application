import calendar
import datetime
import sys
import colorama

def __get_user_input(text):
	"""Gets user input and catchs KeyboardInterrupt"""
	try:
		user_input = input(text)
		return user_input
	except KeyboardInterrupt:
		print()
		sys.exit()

def __split_user_input(inp):
	"""Splits user input"""
	return inp.split() if len(inp.split()) != 0 else [""]

def __print_invalid_input_error():
	print(colorama.Fore.RED + "Invalid command" + colorama.Style.RESET_ALL)

def __exec_command(inp):
	"""Checks for any command calling"""
	splitted = __split_user_input(inp)
	if splitted[0] == "now":
		print(datetime.datetime.now())
	elif splitted[0] == "day":
		print(datetime.datetime.today())
	elif splitted[0] == "exit":
		exit()
	elif splitted[0] == "":
		pass
	else:
		__print_invalid_input_error()


def main():
	colorama.init()
	while True:
		user_input = __get_user_input("$ ")
		
		# commands
		__exec_command(user_input)

if __name__ == "__main__":
	main()