import sys
thres = 0.0001
out = open(sys.argv[1]+".selected.motif","wb")
for line in open(sys.argv[1]).readlines():
	line = line.strip().split(",")
	motif = line[0]
	p_value = float(line[-1])
	z_value = float(line[-2])
	if z_value > 0 and p_value <= thres:
		print >>out,motif








