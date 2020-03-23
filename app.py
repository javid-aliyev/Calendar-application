import calendar
import datetime
import sys
import colorama

# ! ============================ DECORATORS ===========
def green_wrapper(fn):
	def wrapper():
		print(colorama.Fore.GREEN)
		fn()
		print(colorama.Style.RESET_ALL)
	return wrapper

def blue_wrapper(fn):
	def wrapper():
		print(colorama.Fore.BLUE)
		fn()
		print(colorama.Style.RESET_ALL)

# ! ============================ SECONDARY FUNCTIONS (logic) ===========
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

def __exec_command(inp):
	"""Checks for any command calling"""
	splitted = __split_user_input(inp)
	if splitted[0] == "now":
		__print_now()
	elif splitted[0] == "exit":
		exit()
	elif splitted[0] == "":
		pass
	else:
		__print_invalid_input_error()

# ! ============================ PRINT FUNCTIONS (commands) ===========
def __print_invalid_input_error():
	print(colorama.Fore.RED + "Invalid command" + colorama.Style.RESET_ALL)

@green_wrapper
def __print_now():
	print(datetime.datetime.now())

# ! ============================ MAIN FUNCTION (program entry point) ===========
def main():
	colorama.init()
	while True:
		user_input = __get_user_input("$ ")
		
		# commands
		__exec_command(user_input)

if __name__ == "__main__":
	main()