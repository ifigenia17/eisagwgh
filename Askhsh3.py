s = raw_input()
list1 = map(int, s.split())
list2 = []
print list1
for index,value in enumerate(list1):
	if value == 0: 
		tmp = list1.pop(index)
		list1.append(value)
print list1