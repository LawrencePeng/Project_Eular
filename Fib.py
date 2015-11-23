list = [2,8]
while list[-1] < 400000000000000:
	list.append(4 * list[-1] + list[-2])
fList = [x for x in list[:len(list) - 1]]
print sum(fList)
