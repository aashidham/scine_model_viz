import json, pdb
import math, model, numpy
import probe_shape

import spice
import the_platform
from copy import deepcopy
import scipy.integrate

def insert_scine(probedata_env, params, derived):
        compartments = params['compartments']
        A_membrane = derived['A_membrane']
        part_idx = probe_shape.build_table(probedata_env,compartments)
        print part_idx
        assert len(part_idx) == int(params['compartments'])+1
        R_seal=[]
        Rmembrane=[]
        Cmembrane=[]
        for idx in range(1,len(part_idx)):
			curr = part_idx[idx]
			prev = part_idx[idx-1]
			r = probedata_env[prev:curr+1,1]
			neher = probedata_env[prev:curr+1,4]
			sr = neher.astype(float)/(math.pi*2*(r + 50e-9))
			rseali = scipy.integrate.trapz(sr,probedata_env[prev:curr+1,0])
			assert rseali > 0
			R_seal.append(rseali)
			probedata_mem = numpy.column_stack((probedata_env[prev:curr+1,0],probedata_env[prev:curr+1,1]+100e-9))
			curr_area = probe_shape.area(probedata_mem)
			assert curr_area > 0
			Rmembrane.append(1/(params['Mem_cond'] * curr_area) if curr_area > 0 else 1e20)
			Cmembrane.append(curr_area*0.01 if curr_area > 0 else 1e-20)
        derived['R_seal_i'] = R_seal
        derived['Rmembrane_i'] = Rmembrane
        derived['Cmembrane_i'] = Cmembrane
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
        cir_path = model.simple.generate('data/short-spike', the_platform.file('model1.cir'), p)
        spice.ac_analysis(cir_path, -5, 5)
