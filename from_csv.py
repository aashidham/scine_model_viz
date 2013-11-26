import csv
import json
import os
import sys
import unittest
import subprocess
from probe_shape import *

import insert_scine
import model.simple
import progression
import the_platform
import numpy, math, scipy.integrate
import probe_shape

def closest(a,val):
	return min(range(len(a)), key=lambda i: abs(a[i]-val))
	

def run(sid,low_env,high_env):
    # Build up experimental samples.
    fn = str(sid)+"/"+str(sid)+".csv"
    print 'reading from %s..' % fn
    f = open(fn)
    c = csv.reader(f)
    samples = [{}]
    try:
        for row in c:
            if row[0][0] == '#':
                continue

            if len(row) == 5:
                name, start, stop, points, sampling = row
                if sampling == '0':
                    progress = progression.Linear
                elif sampling == '1':
                    progress = progression.Logarithmic
                else:
                    raise Exception('sampling == "%s"' % sampling)
                progress = progress(float(start), float(stop), int(points))

            elif len(row) == 2:
                name, constant = row
                progress = progression.Constant(float(constant))

            else:
                raise Exception('CSV format borked -- len(row) = %i, row = %s' % (len(row), row))

            try:
                new_samples = []
                while True:
                    v = progress.next()
                    for sample in samples:
                        sample = dict(sample)
                        sample[name] = v
                        new_samples.append(sample)
            except StopIteration:
                samples = new_samples
    except StopIteration:
        pass

    probedata_file = str(sid)+"/"+str(sid)+"_probe_shape.txt"
    probedata = eval(open(probedata_file).read())
    probedata = numpy.array(probedata)
    
    #intra goes from 0 to low_idx, env goes from low_idx to high_idx, and extra goes from high_idx to end. low_idx and high_idx are double counted in both intra / extra and env, FYI.
    low_idx = closest(probedata[:,0],low_env)
    high_idx = closest(probedata[:,0],high_env)
    probedata_env = probedata[low_idx:high_idx+1]
    probedata_intra = probedata[0:low_idx+1]
    probedata_extra = probedata[high_idx:]
    probedata_mem = numpy.column_stack((probedata_env[:,0],probedata_env[:,1]+100e-9))
    
    A_intra=area(probedata_intra)
    A_env=area(probedata_env)
    A_membrane=area(probedata_mem) + math.pi*probedata_mem[0,1]**2
    A_extra=area(probedata_extra)
    L_intra=arc_length(probedata_intra)
    L_env=arc_length(probedata_env)
    L_extra=arc_length(probedata_extra)
    
    cpe_bounds_intra = material_boundaries(probedata_intra)
    cpe_bounds_extra = material_boundaries(probedata_extra)
    cpes = []
    for idx in range(1,len(cpe_bounds_intra)):
    	curr = cpe_bounds_intra[idx]
    	prev = cpe_bounds_intra[idx-1]
    	cpe_area = area(probedata_intra[prev:curr+1])
    	if prev == 0:
    		cpe_area = cpe_area + math.pi*probedata[0,1]**2
    	cpe_alpha = probedata_intra[prev,2]
    	cpe_k = probedata_intra[prev,3]
    	id = "cpe_intra_"+str(idx)
    	name = "Xintracpe_i_"+str(idx)
    	cpes.append({"type":"intra","id":id,"area":cpe_area,"alpha":cpe_alpha,"k":cpe_k,"name":name})    
    
    for idx in range(1,len(cpe_bounds_extra)):
    	curr = cpe_bounds_extra[idx]
    	prev = cpe_bounds_extra[idx-1]
    	cpe_area = area(probedata_extra[prev:curr+1])
    	cpe_alpha = probedata_extra[prev,2]
    	cpe_k = probedata_extra[prev,3]
    	id = "cpe_extra_"+str(idx)
    	name = "Xextracpe_i_"+str(idx)
    	cpes.append({"type":"extra","id":id,"area":cpe_area,"alpha":cpe_alpha,"k":cpe_k,"name":name})

    derived_params = {
		'A_intra': A_intra,
		'A_env': A_env,
		'A_membrane': A_membrane,
		'A_extra': A_extra,
		'L_intra': L_intra,
		'L_env': L_env,
		'L_extra': L_extra,
		}
 
    
    # For all samples,
    root = the_platform._root
    for i, sample in enumerate(samples):
		the_platform.set_root(os.path.join(*(root + ['trial=%i' % i])))
		# store the params to be used in the simulation,
		f = open(the_platform.file('parameters.json'), 'w')
		f.write(json.dumps(sample))
		f.close()
		# and run the simulation.
		print sample
		assert len(probedata_env) > int(sample['compartments'])
		insert_scine.insert_scine(probedata,probedata_env,sample,derived_params,cpes)
    
    root = "/".join(root)
    
    os.system('find %s -type d -links 2 | parallel -v  --gnu --sshlogin 32/ubuntu@ec2-54-200-54-145.us-west-2.compute.amazonaws.com --transfer --return {}/the.data "ngspice -p {}/model1.cir < {}/spice.input"' % root)

    for i in range(len(samples)):
	   mag_plot_fn = root + "/trial=%i/plot-mag.png" % i
	   phase_plot_fn = root + "/trial=%i/plot-phase.png" % i
	   data = root + "/trial=%i/the.data" % i
	   subprocess.check_call("gnuplot -e \"set term png; set output '%s'; set logscale x; plot '%s' using 1:2 with linespoints notitle\"" % (mag_plot_fn, data), shell=True)
	   subprocess.check_call("gnuplot -e \"set term png; set output '%s'; set logscale x; plot '%s' using 3:4 with linespoints notitle\"" % (phase_plot_fn, data), shell=True)

if __name__ == '__main__':
    assert len(sys.argv) == 2
    _, csv_fn = sys.argv
    run(csv_fn)
