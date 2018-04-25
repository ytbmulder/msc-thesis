#!python3

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# TODO: use latex for text: https://matplotlib.org/users/usetex.html
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

base_path = os.path.dirname(os.path.realpath(__file__))

fig = plt.figure()
ax = fig.add_subplot(111)

# Uni-directional interconnect constants [GB/s/lane].
gen1 = 0.25
gen2 = 0.5
gen3 = 0.9846
gen4 = 1.969
gen5 = 3.938
ocapi = 25/8

# Plot DRAM bandwidth in GB/s.
location = os.path.join(base_path, "1-fritz-bw-dram.csv")
data = np.genfromtxt(location, delimiter=',', names=['year', 'bw'])
ax.plot(data['year'], data['bw'], 'go-', label="DRAM BW / CPU socket", markersize=4)

# Fit test.
x = data['year']
y = data['bw']

p = np.polyfit(x, np.log(y), 1)
ax.semilogy(x, np.exp(p[0] * x + p[1]), 'g--')

# Linear fit.
#x = data['year']
#y = data['bw']
#y_ln = np.log10(y)

#n = data.shape[0]
#A = np.array(([[x[j], 1] for j in range(n)]))
#B = np.array(y_ln[0:n])
#B = np.array(y[0:n])

#X = np.linalg.lstsq(A, B)[0]
#a = X[0]
#b = X[1]

#fit = a * x + b



#p = np.polyfit(x, np.log(y), 1)
#ax.semilogy(x, p[0] * x + p[1], 'g--')




# fit 2
#A = np.vstack([x, np.ones(len(x))]).T
#print(A)
#m, c = np.linalg.lstsq(A, np.log(y))[0]
#print(m, c)
#ax.plot(x, m*x + c, 'g--')



# Plot Network bandwidth in GB/s.
location = os.path.join(base_path, "1-fritz-bw-net.csv")
data = np.genfromtxt(location, delimiter=',', names=['year', 'bw'])
ax.plot(data['year'], data['bw']/1000, 'ro-', label="Network BW / cable", markersize=4)

# Plot PCIe bandwidth in GB/s for x16 slots.
# PCI-X 1.0 and 2.0: [1998, 2003] [1.06, 4.266]
# OpenCAPI 2018 16*ocapi
pcie_y = [2003, 2007.25, 2011.00, 2017.50, 2019.00]
pcie_b = [16*gen1, 16*gen2, 16*gen3, 16*gen4, 16*gen5]
ax.plot(pcie_y, pcie_b, 'yo-', label="PCIe BW / 16 lanes", markersize=4)

# Plot SSD bandwidth in GB/s.
location = os.path.join(base_path, "1-fritz-bw-ssd.csv")
data = np.genfromtxt(location, delimiter=',', names=['year', 'bw'])
ax.plot(data['year'], data['bw']/1000, 'bo-', label="Storage BW / device", markersize=4)
# Fit from Edu.
#x = data['year']
#y = 0.1256 * x - 249.94
#ax.plot(x, y, 'b--')

# TEST

#x = data['year']
#x = np.array(x, dtype=np.float128)
#k = 1 # y-intercept. value of y where line crosses x=0 axis
#m = 0.00075 # slope of line
#y = k * np.power(m * x, 10)
#ax.plot(x, y, 'g--')


# TODO: draw straight line through each data set

# Plot setup
ax.set_yscale('log')
#plt.axis([1993, 2022, 0.001, 1000])
#for axis in [ax.yaxis]: # Custom y tick formatter.
#  axis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x}"))
ax.set_xlabel("Year")
ax.set_ylabel("Bandwidth [GB/s]")
ax.yaxis.grid(True) #ax.grid()
plt.legend(loc=2)

# Output image filename is the name of the script without its extension, plus ".pdf".
filename = os.path.splitext(os.path.basename(__file__))[0] + ".pdf"
location = os.path.join(base_path, filename)
plt.savefig(location)
