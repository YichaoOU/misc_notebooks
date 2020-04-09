import glob
import numpy as np
def get_p_value(label,motif): 
	pvalue = "/users/PHS0293/ohu0404/project/Brugia/control_set_mapping/my_label_final_motifs.pwm.fimo.mhit.count.tsv.pvalue.csv"
	pvalue = pvalue.replace("my_label",label)
	# print pvalue
	# exit()
	for line in open(pvalue).readlines():
		line = line.strip().split(",")
		# motif = line[0]
		if motif == line[0]:
			return float(line[-1])
	
	
def cal_avg_p_value(file,out):
	# my_dict = {}
	for line in open(file).readlines():
		line = line.strip().split()
		# print line
		# exit()
		motif1 = line[0]
		motif2 = line[2]
		motif3 = line[4]
		label1 = line[1]
		label2 = line[3]
		label3 = line[5]
		p_value1 = get_p_value(label1,motif1)
		p_value2 = get_p_value(label2,motif2)
		p_value3 = get_p_value(label3,motif3)
		avg = np.mean([p_value1,p_value2,p_value3])
		outline = line+[str(avg)]
		print >>out," ".join(outline)
		# my_dict[motif1] = avg
	# return my_dict	
motif_list = glob.glob("/users/PHS0293/ohu0404/project/Brugia/stage_specific_motif/tomtom_compare/*.motifs")


for file in motif_list:
	print file
	stage = file.split("/")[-1].split(".")[0]
	
	out = open(stage+".selected_motifs.with.pvalue.tsv","wb")
	my_dict = cal_avg_p_value(file,out)
	# for k in my_dict:
		# v = my_dict[k]
		# print >>out," ".join([k,str(v)])
	out.close()

















