# input csv format
# output motif list
import pandas as pd
import numpy as np
from scipy.stats import norm
import sys
def z_value(obs,s,n_pos,iter):
	my_list = []
	for i in range(iter):
		# df[df['B']>0.5]['A'].sample(replace=True,n=100).sum()
		temp = s.sample(replace=True,n=n_pos).sum()
		my_list.append(temp)
	my_mean = np.mean(my_list)
	my_std = np.std(my_list)
	# print "std",my_std
	my_z = (obs - my_mean)/my_std
	return abs(my_z)
	

data = pd.read_csv(sys.argv[1],delimiter = ",")
motifs=list(data.columns)[:-1]
label = list(data.columns)[-1]
output = sys.argv[2]
out = open(output,"wb")

for m in motifs:
	
	neg_series = data[data[label] == "neg"][m]
	pos_series = data[data[label] == "pos"][m]
	my_obs = pos_series.sum()
	n_pos = int(pos_series.shape[0])
	my_z = z_value(my_obs,neg_series,n_pos,iter=1000)
	p_value = norm.sf(my_z)
	# print m,p_value
	print >>out,m,p_value
		

out.close()






















