from random import randint as rd

def sort(alist):
	print alist 
	if len(alist)>1:
		mid = len(alist)>>1
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		sort(lefthalf)
		sort(righthalf)

		i = 0
		j = 0
		k = 0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1

		print 'merging', alist

alist = []
for i in xrange(10):
	alist.append(rd(10,99))
sort(alist)