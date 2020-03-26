#!/usr/bin/python3
import calendar
import datetime
import os
import colorama
import time

# ! ============================ DECORATORS ===========
# ! =======================================
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

def cyan_wrapper(fn):
	def wrapper():
		print(colorama.Fore.CYAN)
		fn()
		print(colorama.Style.RESET_ALL)
	return wrapper

# ! ============================ HELP ===========
# ! =======================================
@cyan_wrapper
def __help():
	commands = ["now",
				"day",
				"year",
				"curryear",
				"currmonth",
				"help",
				"clear",
				"exit"]
	for num, command in enumerate(commands, 1):
		print(f"{num}. {command}")

# ! ============================ ERRORS ===========
# ! =======================================
@red_wrapper
def __print_invalid_input_error():
	print("Invalid command")

@red_wrapper
def __print_invalid_year_error():
	print("Invalid year")

@red_wrapper
def __print_invalid_month_error():
	print("Invalid month")

# ! ============================ PRINT FUNCTIONS (commands) ===========
# ! =======================================
@blue_wrapper
def __print_now():
	print(f"{datetime.datetime.now()} UTC{__get_utc()}")

@green_wrapper
def __print_curr_year():
	cal.pryear(datetime.datetime.now().year)

@green_wrapper
def __print_curr_month():
	now = datetime.datetime.now()
	cal.prmonth(now.year, now.month)

def __print_year():
	try:
		year = int(__get_user_input("The year you want to see: "))
		print(colorama.Fore.GREEN)
		cal.pryear(year)
		print(colorama.Style.RESET_ALL)
	except ValueError:
		__print_invalid_year_error()

@blue_wrapper
def __print_curr_day():
	# POINT .001
	days = ["Monday", "Tuesday", "Wednesday",
			"Thursday", "Friday", "Saturday",
			"Sunday"]
	result = ""
	now = datetime.datetime.now()
	bazz = calendar.weekday(now.year, now.month, now.day)
	for i in range(len(days)):
		if i == bazz:
			result += days[i]
	result += f". {now.day} {calendar.month_name[now.month]}"
	print(result)

def __print_time_to():
	date = __get_user_input("Date: ")
	print(colorama.Fore.BLUE)
	now = datetime.datetime.now()
	try:
		print(now, datetime.datetime.strptime(date, "%Y-%m-%d") - now, sep="\n")
	except ValueError:
		return
	finally:
		print(colorama.Style.RESET_ALL)

def __print_time_for():
	__print_curr_day()
	__print_now()
	try:
		daysfor = int(__get_user_input("Days: "))
		print(colorama.Fore.BLUE)
		now = datetime.datetime.now()
		print(now + datetime.timedelta(days=daysfor))
		print(colorama.Style.RESET_ALL)
	except ValueError:
		return

# ! ============================ SECONDARY FUNCTIONS (logic) ===========
# ! =======================================
def __get_utc():
	return time.localtime().tm_zone

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
	elif inp == "curryear":
		__print_curr_year()
	elif inp == "currmonth":
		__print_curr_month()
	elif inp == "day":
		__print_curr_day()
	elif inp == "timeto":
		__print_time_to()
	elif inp == "timefor":
		__print_time_for()
	elif inp == "help":
		__help()
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
# ! =======================================
def main():
	global cal
	cal = calendar.TextCalendar()
	colorama.init()
	while True:
		user_input = __get_user_input("$ ")
		__exec_command(user_input)

if __name__ == "__main__":
	main()
