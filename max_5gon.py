import itertools
# create a generator that determines the inside pentagon ring (represent data as a list)
# filter our anything in which two adjacent numbers >= value
# fill in & check if outer rows > 16 (try all combinations)

def createPentagonCombos(numbers, shape_c, upper): # 10, 5, 16
	#input is range of working numbers (i.e 1-5, 1-10), 
	#shape_c (int -> 3,5,7...), and upper (int -> 16 in this case)
	r_list = [num for num in range(1,numbers+1)]
	val_shapes = list(itertools.combinations(r_list, shape_c))
	return map(lambda tup: list(itertools.permutations(tup)), val_shapes)


def valid_interior(tup, upper, numbers): 
	num_list_destr = [num for num in range(1, numbers+1)]
	ret_list = list()
	for elem in tup:
		num_list_destr.remove(elem)
	
	for index in range(len(tup)):
		leaf = upper - (tup[index] + tup[(index+1)%len(tup)])
		if(leaf in num_list_destr):
			ret_list.append((leaf, tup[index], tup[(index+1)%len(tup)]))
			num_list_destr.remove(leaf)
		else: return None
	return ret_list

#create list of 2d tuples, each big tuple containing a ring and small sub containing a branch
def generate_2d_tuplist(numbers, shape_c, upper):
	val_tup = createPentagonCombos(numbers, shape_c, upper)
	final_list = list()
	for l_tup in val_tup:
		for tup in l_tup:
			if(valid_interior(tup, upper, numbers) != None):
				final_list.append(valid_interior(tup, upper, numbers))
	return final_list


def create_string(numbers, shape_c, upper):
	val_list = generate_2d_tuplist(numbers, shape_c, upper)
	for ans_list in sorted(val_list):
		ans_list = sorted(ans_list, key = lambda x : x[0])
		#there has to be a way to represent this data in and int format - figure it out
		ans_list = map((lambda tup: list(tup)), ans_list)
		print(ans_list)


print(create_string(10, 5, 14))