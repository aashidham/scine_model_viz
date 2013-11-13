import numpy, math, scipy.integrate

def arc_length(a):
	total_len = 0
	for i in range(1,len(a)):
		curr = a[i,1:2]
		prev = a[i-1,1:2]
		total_len = total_len + numpy.linalg.norm(curr-prev)
	return total_len

def area(a):
	return 2*math.pi*scipy.integrate.trapz(a[:,1],a[:,0])


def x_partition(y,num):
	to_return = [len(y)-1]
	last_y = y[len(y)-1]
	y_per_component = last_y/float(num)
	print y_per_component
	for i in range(1,num):
		curr_y = last_y - i*y_per_component
		for j in range(len(y)):
			if y[j] < curr_y and y[j+1] > curr_y:
				to_return.append(j)
	to_return.append(0)
	to_return.reverse()
	return to_return


def build_table(np_probedata,num_compartments):
	neher = np_probedata[:,4]
	radius = np_probedata[:,1]
	seal_resistance = scipy.integrate.cumtrapz(neher/(math.pi*2*radius),np_probedata[:,0])
	part_idx = x_partition(seal_resistance,int(num_compartments))
	return part_idx
	
def sr_array(np_probedata,part_idx):
	result = []
	for idx in range(1,len(part_idx)):
		curr = part_idx[idx]
		prev = part_idx[idx-1]
		r = np_probedata[prev:curr,1]
		neher = np_probedata[prev:curr,4]
		sr = neher.astype(float)/(math.pi*2*(r + 50e-9))
		result.append(scipy.integrate.trapz(sr,np_probedata[prev:curr,0]))
	return result

"""
def dist(a,b):
	a = numpy.array(a)
	b = numpy.array(b)
	return numpy.linalg.norm(a-b)


def build_table(probedata):
	arc_lengths = []
	for idx in range(len(probedata)):
		prev = probedata[max(0,idx-1)] #so that idx-1 is never negative
		curr = probedata[idx]
		arc_lengths.append(dist(prev,curr))
	cum_arc_lengths = numpy.cumsum(arc_lengths)
	x_values = [elem[0] for elem in probedata]
	x_idx = x_partition(cum_arc_lengths,
"""