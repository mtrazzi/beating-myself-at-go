import numpy as np
import sys
import os

def print_map(map):
	dic = {0: ".", 1: "X", 2: "O", 3: "*"}
	map = put_hoshi(map)
	sys.stdout.write("   ")
	for j in range(len(map)):
		sys.stdout.write("%2d " % (j + 1))
	print
	for i in range(len(map)):
		sys.stdout.write("%2d " % (i + 1))
		for x in map[i]:
			sys.stdout.write("%2c " % dic[x])
		print

def	put_hoshi(map):
	size = len(map)
	if (size != 19):
		return map
	for i in (range(size)):
		for j in (range(size)):
			if (i == 3 or i == 9 or i == 15):
				if (j == 3 or j== 9 or j == 15):
					if (map[i][j] == 0):
						map[i][j] = 3
	if (map[9][9] == 0):
		map[9][9] = 3
	return map

def	empty_map(size):
	return np.zeros((size, size))

def	add_point(map, type, x, y):
	map[x - 1][y - 1] = type
	return (map)

map = empty_map(int(sys.argv[1]))
user_input = ""
counter = 0;
os.system("clear")
print_map(map)
user_input = raw_input("Your next move (type \"exit\" to quit): $>")
while (user_input != "exit"):
	add_point(map, counter + 1, int(user_input.split()[0]), int(user_input.split()[1]))
	os.system("clear")
	print_map(map)
	counter = (counter + 1) % 2
	user_input = raw_input("Your next move (type \"exit\" to quit): $>")
os.system("clear")
