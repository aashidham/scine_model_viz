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
	seal_resistance = []
	for elem in probedata:
		neher = elem[4]
		r = elem[1]
		curr_sr = neher/(math.pi*2*(r + 50e-9))
		seal_resistance.append(curr_sr)
	seal_resistance = numpy.cumsum(seal_resistance)
	part_idx = x_partition(seal_resistance,5)
	print part_idx
	np_probedata = numpy.array(probedata)
	for idx in range(1,len(part_idx)):
		curr = part_idx[idx]
		prev = part_idx[idx-1]
		avg_r = numpy.mean(np_probedata[prev:curr,1])
		avg_neher = numpy.mean(np_probedata[prev:curr,4])
		print avg_neher/(math.pi*2*(avg_r + 50e-9))
	print "with real integration:"
	for idx in range(1,len(part_idx)):
		curr = part_idx[idx]
		prev = part_idx[idx-1]
		r = np_probedata[prev:curr,1]
		neher = np_probedata[prev:curr,4]
		sr = neher.astype(float)/(math.pi*2*(r + 50e-9))
		print scipy.integrate.trapz(sr,np_probedata[prev:curr,0])

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