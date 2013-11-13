import numpy, math, scipy.integrate


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


def build_table(probedata):
	np_probedata = numpy.array(probedata)
	neher = np_probedata[:,4]
	radius = np_probedata[:,1]
	seal_resistance = scipy.integrate.cumtrapz(neher/(math.pi*2*(radius + 50e-9)),np_probedata[:,0])
	part_idx = x_partition(seal_resistance,5)
	return part_idx
	"""
	result = []
	for idx in range(1,len(part_idx)):
		curr = part_idx[idx]
		prev = part_idx[idx-1]
		r = np_probedata[prev:curr,1]
		neher = np_probedata[prev:curr,4]
		sr = neher.astype(float)/(math.pi*2*(r + 50e-9))
		result.append(scipy.integrate.trapz(sr,np_probedata[prev:curr,0]))
	print result
	import pdb; pdb.set_trace()
	"""

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