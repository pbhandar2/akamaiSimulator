
import numpy as np;
from scipy.interpolate import spline;
import matplotlib.pyplot as plt;
import os;
import math;
from scipy.signal import savgol_filter

cwd = os.getcwd();
data_location = "../output/data.out";

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

x = bin
y = l2_hits

yhat = savgol_filter(y, 51, 3)
#yhat = savitzky_golay(y, 51, 3) # window size 51, polynomial order 3
fontsize_value = 30


plt.plot(x,y)
plt.plot(x,yhat, color='red', linewidth=2.0)
plt.ylim(0, np.amax(y))
plt.xlabel("Reuse Distance", fontsize=fontsize_value )
plt.ylabel("Possible L2 hits per L1 hit at reuse distance x", fontsize=fontsize_value )
plt.title("19.21.108.123.anon", fontsize=fontsize_value )
plt.xlim(0, bin_count-1)
plt.show()
