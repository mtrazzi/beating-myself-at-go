import numpy as np
import sys
import os
import rules

def print_map(map):
	dic = {0: ".", 1: "X", 2: "O", 3: "*"}
	map = change_hoshi(map)
	sys.stdout.write("   ")
	for j in range(len(map)):
		sys.stdout.write("%2d " % (j + 1))
	print
	for i in range(len(map)):
		sys.stdout.write("%2d " % (i + 1))
		for x in map[i]:
			sys.stdout.write("%2c " % dic[x])
		print
	map = change_hoshi(map)

def	change_hoshi(map):
	size = len(map)
	if (size != 19):
		return map
	for i in (range(size)):
		for j in (range(size)):
			if (i == 3 or i == 9 or i == 15):
				if (j == 3 or j== 9 or j == 15):
					if (map[i][j] == 0 or map[i][j] == 3):
						map[i][j] = 3 - map[i][j]
	return map

def	empty_map(size):
	return np.zeros((size, size))

def	add_point(map, type, x, y):
	map[x - 1][y - 1] = type
	return (map)

def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def is_valid_input(s, map):
	if (len(s.split(None)) != 2):
		return False
	if ((not RepresentsInt(s.split()[0])) or (not RepresentsInt(s.split()[1]))):
		return False
	x = int(s.split()[0])
	y = int(s.split()[1])
	return ((x > 0 and x <= len(map)) and (y > 0 and y <= len(map)) \
	and (map[x - 1][y - 1] == 0) and rules.have_liberties(map, x - 1, y - 1))

def get_input(map):
	user_input = ""
	while (user_input != "exit" and (not is_valid_input(user_input, map))):
		os.system("clear")
		print_map(map)
		if (user_input != ""):
			print("Move badly formated : must type \"x y\" with x and y integers")
			print("Example : \"2 3\"")
			print("Intersection must be empty (must be \'.\' or *)")
			print("Stone must be next to other empty intersection or capture a group")
		user_input = raw_input("Your next move (type \"exit\" to quit): $>")
	if (user_input == "exit"):
		sys.exit()
	return (int(user_input.split(None)[0]), int(user_input.split(None)[1]))

map = empty_map(int(sys.argv[1]))
counter = 0;
while (1):
	x, y = get_input(map)
	add_point(map, counter + 1, x, y)
	counter = (counter + 1) % 2
	rules.kill_dead_stones(map, counter + 1)
	#while (raw_input("") != ""):
	#	pass
