import calendar
import datetime
import os
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
	return wrapper

def red_wrapper(fn):
	def wrapper():
		print(colorama.Fore.RED)
		fn()
		print(colorama.Style.RESET_ALL)
	return wrapper

# ! ============================ PRINT FUNCTIONS (commands) ===========
@red_wrapper
def __print_invalid_input_error():
	print("Invalid command")

@red_wrapper
def __print_invalid_year_error():
	print("Invalid year")

@green_wrapper
def __print_now():
	print(datetime.datetime.now())

def __print_year():
	try:
		year = int(__get_user_input("The year you want to see: "))
		print(colorama.Fore.GREEN)
		cal.pryear(year)
	except ValueError:
		__print_invalid_year_error()
	print(colorama.Style.RESET_ALL)

# ! ============================ SECONDARY FUNCTIONS (logic) ===========
def __get_user_input(text):
	"""Gets user input and catchs KeyboardInterrupt"""
	try:
		user_input = input(text)
		return user_input
	except KeyboardInterrupt:
		print()
		exit()

def __exec_command(inp):
	"""Checks for any command calling"""
	if inp == "now":
		__print_now()
	elif inp == "year":
		__print_year()
	elif inp == "exit":
		exit()
	elif inp == "clear":
		__clear_terminal()
	elif inp == "":
		pass
	else:
		__print_invalid_input_error()

def __clear_terminal():
	os.system("clear")

# ! ============================ MAIN FUNCTION (program entry point) ===========
def main():
	global cal
	cal = calendar.TextCalendar()
	colorama.init()
	while True:
		user_input = __get_user_input("$ ")
		__exec_command(user_input)

if __name__ == "__main__":
	main()