from random import randint as rd


def sort(arr, start, end):
	if start >= end:
		return
	mid = (start+end)>>1
	print 'mid =', mid, 'start =', start, 'end =', end 
	sort(arr, start, mid)
	sort(arr, mid+1, end)
	print arr, start, mid, end
	merging(arr, start, mid, end)

def merging(a, start, mid, end):
	tmp = [0]*(end-start+1)
	i = start
	j = mid + 1
	k = 0
	while i<=mid and j<=end:
		if a[i] <= a[j]:
			tmp[k] = a[i]
			i += 1
		else:
			tmp[k] = a[j]
			j += 1
		k += 1

	while i <= mid:
		tmp[k] = a[i]
		i += 1
		k += 1
	while j <= end:
		tmp[k] = a[j]
		j += 1
		k += 1
	for k in xrange(len(tmp)):
		a[start+k] = tmp[k]

alist = []
for i in xrange(10):
	alist.append(rd(10,99))
sort(alist, 0, len(alist)-1)
print alist