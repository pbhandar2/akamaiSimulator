
import numpy as np;
from scipy.interpolate import spline;
import matplotlib.pyplot as plt;
import os;
import math;

cwd = os.getcwd();
data_location = cwd+"/data.out";

f = open(data_location, 'r');
l2_hits = []
bin_count = 0
bin = []
for line in f:
	if len(line.split(",")) > 1:
		line = line.replace("\n", "")
		records = line.split(",")
		l2_hits.append(float(records[3]))
		bin.append(bin_count)
		bin_count = bin_count + 1

x_sm = np.array(bin)
y_sm = np.array(l2_hits)

x_smooth = np.linspace(x_sm.min(), x_sm.max(), math.floor(bin_count/20))
y_smooth = spline(bin, l2_hits, x_smooth)

fontsize_value = 30

canvas = plt.figure()
# Define the matrix of 1x1 to place subplots
# Placing the plot1 on 1x1 matrix, at pos 1
sp1 = canvas.add_subplot(1,1,1, axisbg='w')
#sp1.plot(x, y, 'red', linewidth=2)
plt.plot(x_smooth, y_smooth, 'red', linewidth=1)
plt.xticks(np.arange(0, bin_count, step=50));
plt.xticks(fontsize=fontsize_value-7, rotation=90)
plt.yticks(fontsize=fontsize_value )

plt.xlabel("Reuse Distance", fontsize=fontsize_value )
plt.ylabel("Possible L2 hits per L1 hit at reuse distance x", fontsize=fontsize_value )
plt.title("19.21.108.123.anon", fontsize=fontsize_value )
plt.xlim(0, bin_count-1)
plt.show()




