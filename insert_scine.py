import json, pdb
import math, numpy
import model.simple2
import probe_shape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from cStringIO import StringIO

import spice
import the_platform
from copy import deepcopy
import scipy.integrate

def insert_scine(probedata,probedata_env, params, derived,cpes):
        compartments = params['compartments']
        A_membrane = derived['A_membrane']
        part_idx = probe_shape.build_table(probedata_env,compartments)
        print part_idx
        
        plt.figure()
        plt.plot(probedata[:,0],probedata[:,1])
        materials_idx = probe_shape.material_boundaries(probedata)
        color_list = plt.cm.Set3(numpy.linspace(0, 1, len(materials_idx)))[:,0:3]
        for idx in range(1,len(materials_idx)):
        	curr = materials_idx[idx]
        	prev = materials_idx[idx-1]
        	plt.fill_between(probedata[prev:curr+1,0],0,probedata[prev:curr+1,1],color=color_list[idx])
        la = max(probedata[:,1])
        for idx in part_idx:
        	plt.plot([probedata_env[idx,0]]*20,numpy.linspace(0,la,20),'black')
        sio = StringIO()
        plt.savefig(sio)
        f = open(the_platform.file('probe.png'), 'wb')
        f.write(sio.getvalue())
        f.close()
        plt.clf()
        
        R_seal=[]
        Rmembrane=[]
        Cmembrane=[]
        CPE_alpha = []
        CPE_k = []
        area = []
        for idx in range(1,len(part_idx)):
			curr = part_idx[idx]
			prev = part_idx[idx-1]
			CPE_alpha.append(probedata_env[prev,2])
			CPE_k.append(probedata_env[prev,3])
			r = probedata_env[prev:curr+1,1]
			neher = probedata_env[prev:curr+1,4]
			sr = neher.astype(float)/(math.pi*2*(r + 50e-9))
			rseali = scipy.integrate.trapz(sr,probedata_env[prev:curr+1,0])
			assert rseali > 0
			R_seal.append(rseali)
			probedata_mem = numpy.column_stack((probedata_env[prev:curr+1,0],probedata_env[prev:curr+1,1]+100e-9))
			curr_area = probe_shape.area(probedata_mem)
			assert curr_area > 0
			area.append(curr_area)
			Rmembrane.append(1/(params['Mem_cond'] * curr_area) if curr_area > 0 else 1e20)
			Cmembrane.append(curr_area*0.01 if curr_area > 0 else 1e-20)
        derived['R_seal_i'] = R_seal
        derived['Rmembrane_i'] = Rmembrane
        derived['Cmembrane_i'] = Cmembrane
        derived['CPE_extremes'] = cpes
        derived['CPE_alpha'] = CPE_alpha
        derived['CPE_k'] = CPE_k
        derived['area'] = area
        print derived
        f = open(the_platform.file('derived_params.json'), 'w')
        f.write(json.dumps(derived))
        f.close()
        # Mix together all params, the model will need them all. And
        # do the analysis.
        p = dict(params)
        for k, v in derived.items():
            assert k not in p
            p[k] = v
	cir_path = model.simple2.generate(the_platform.file('model1.cir'), p,cpes)
        spice.ac_analysis(cir_path, -5, 5)
