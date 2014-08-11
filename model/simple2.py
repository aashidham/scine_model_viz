import os
import re
import subprocess
import tempfile

import model.ladder_cpe



def generate(filename, params,cpes):
	netlist = ["""* Spice netlister for gnetlist
CStray 0 electrode_bus %s""" % params['CStray']]
	netlist.append('RStray 0 electrode_bus %s'% params['RStray'])
	netlist.append('Rbath 0 solution_bus %s'% params['Rbath'])
	netlist.append('Cwholecell solution_bus cell_bus %s'%params['Cwholecell'])
	netlist.append('Rwholecell solution_bus cell_bus %s'%params['Rwholecell'])
	netlist.append('R_pene cell_bus Rpene_bus %s'%params['R_pene'])
	
	#in the below, need to substitute for global area
	netlist.append('i1 0 cell_bus pulse(0    8e-010      25ms       1ms        1ms        25ms  100ms)')
	netlist.append('.model memr hh (area=1e-4)')
	netlist.append('amen cell_bus 0 memr')
	
	netlist.append('%s\n\n%s\n%s\n') #first for extreme_cpes, second for env_region, third for the generated_ladders
	#netlist.append('Vcell cell_bus 0 1v ac')
	#netlist.append('.model cell_potential filesource (file="data/short-spike", amploffset=[0], amplscale=[1])')
	netlist = '\n'.join(netlist)
	
	extreme_cpes = []
	for cpe in cpes:
		if cpe["type"] == "intra":
			extreme_cpes.append(cpe["name"] + " cell_bus electrode_bus " + cpe["id"])
		else:
			extreme_cpes.append(cpe["name"] + " solution_bus electrode_bus " + cpe["id"])
	extreme_cpes = '\n'.join(extreme_cpes)
	
	env_region = []
	for i in range(int(params['compartments'])):
		if i==0:
			env_region.append("R_seal_i_0 compartment_0 solution_bus %s" % params['R_seal_i'][i])
		else:
			env_region.append("R_seal_i_%i compartment_%i compartment_%i %s" % (i,i,i-1,params['R_seal_i'][i]))
		env_region.append("Xsheathedcpe_i_%i compartment_%i electrode_bus sheathed_cpe_i_%i" % (i,i,i))
		#env_region.append("Rmembrane_i_%i compartment_%i cell_bus %s" % (i,i,params['Rmembrane_i'][i]))
		#env_region.append("Cmembrane_i_%i compartment_%i cell_bus %s" % (i,i,params['Cmembrane_i'][i]))
		env_region.append("amen_%i cell_bus compartment_%i memr_%i" % (i,i,i))
		env_region.append(".model memr_%i hh (area=%s)" % (i,params['area'][i]))
	env_region = '\n'.join(env_region)
	
	generated_ladders=[]
	for cpe in cpes:
		generated_ladders.extend([''] + model.ladder_cpe.generate(cpe['id'],50,cpe['alpha'],cpe['k']/ (cpe['area'] + 1e-30)))
	for i in range(int(params['compartments'])):
		id = "sheathed_cpe_i_%i" % i
		alpha = params['CPE_alpha'][i]
		k = params['CPE_k'][i]
		area = params['area'][i]
		generated_ladders.extend([''] + model.ladder_cpe.generate(id,50,alpha,k/(area + 1e-30)))
	generated_ladders = '\n'.join(generated_ladders)
	
	to_file = netlist % (extreme_cpes,env_region,generated_ladders)
	f = open(filename, 'w')
	f.write(to_file)
	f.close()
	
	return filename