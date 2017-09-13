import numpy as np

def have_liberties(map, x ,y):
	up = (x > 0 and map[x - 1][y] == 0)
	down = (x < len(map) - 1 and map[x + 1][y] == 0)
	right = (y < len(map) - 1 and map[x][y + 1] == 0)
	left = (y > 0 and map[x][y - 1] == 0)
	return (up or down or right or left)

def is_there_alive_neighbor(map, check_map, x, y, color):
	if (not(x >= 0 and x < len(map) and y >= 0 and y < len(map))):
		return False
	if (check_map[x][y] == 1 or map[x][y] != color):
	 	return False
	print("(%d, %d)" % (x + 1, y + 1))
	check_map[x][y] = 1
	if (have_liberties(map, x, y) and map[x][y] == color):
		print ("have liberties")
		return True
	return (is_there_alive_neighbor(map, check_map, x - 1, y, color) or
		is_there_alive_neighbor(map, check_map, x + 1, y, color) or
		is_there_alive_neighbor(map, check_map, x, y - 1, color) or
		is_there_alive_neighbor(map, check_map, x, y + 1, color))

def is_alive(map, x, y, color):
	print("is (%d, %d) alive ?\n" % (x, y))
	check_map = np.zeros((len(map), len(map)))
	return is_there_alive_neighbor(map, check_map, x, y, color)

def list_of_dead(map, color):
	l = []
	for i in (range(len(map))):
		for j in (range(len(map))):
			#print('(%d, %d) ? %d' % (i, j, is_alive(map, i, j)))
			if (map[i][j] == color and (not(is_alive(map, i, j, map[i][j])))):
				l.append((i, j))
	return l

def	kill_dead_stones(map, color):
	l = list_of_dead(map, color)
	print l
	for p in l:
		map[p[0]][p[1]] = 0

#def	is_valid_move(map, x, y):
#	cpy = numpy.array(map)
#	main.add_point(map, counter )
#
#def triggers_ko(map, old_map, x, y):
#	cpy = np.array(old_map)
#	add_point(map, counter + 1, x, y)
