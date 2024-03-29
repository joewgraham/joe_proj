from netpyne import specs, sim

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg  # if no simConfig in parent module, import directly from cfg module

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Population parameters
netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
netParams.popParams['CA229py'] = {'cellType': 'detailed', 'numCells': 1, 'cellModel': 'HH'}
#netParams.popParams['CA229hoc'] = {'cellType': 'detailed', 'numCells': 1, 'cellModel': 'blank'}


## Cell property rules
cellRule = {'conds': {'cellType': 'PYR'},  'secs': {}} 	# cell rule dict
cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}  														# soma params dict
cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  									# soma geometry
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  		# soma hh mechanism
netParams.cellParams['PYRrule'] = cellRule  

cellRule = netParams.importCellParams(label='CA229py', conds={'pop': 'CA229py'}, fileName='cells/CA_229.py', cellName='MakeCell', importSynMechs=True)

#cellRule = netParams.importCellParams(label='CA229hoc', conds={'pop': 'CA229hoc'}, fileName='cells/CA_229.hoc', importSynMechs=False)




## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': cfg.synMechTau2, 'e': 0}  # excitatory synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}
netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

## Cell connectivity rules
netParams.connParams['S->M'] = { 	#  S -> M label
	'preConds': {'pop': 'S'}, 	# conditions of presyn cells
	'postConds': {'pop': 'M'}, # conditions of postsyn cells
	'probability': 0.5, 			# probability of connection
	'weight': cfg.connWeight, 		# synaptic weight
	'delay': 5,						# transmission delay (ms)
	'synMech': 'exc'}   			# synaptic mechanism
