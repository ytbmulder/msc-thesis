#!python3

import os
import matplotlib.pyplot as plt
import numpy as np

base_path = os.path.dirname(os.path.realpath(__file__))

fig = plt.figure(1)
ax = fig.add_subplot(111)

# TODO: plot IO bw with total number of sockets possible
# plt.plot([2018], [40*gen3*8], 'ro') #intel with total sockets
# TODO: generalize names for processors, for example: Intel E5 2xxx v4 or Opteron 63xx
# TODO: use latex for text: https://matplotlib.org/users/usetex.html

# Release quarters:
# Q1 = 201x.25
# Q2 = 201x.50

# Uni-directional interconnect constants [GB/s/lane].
gen1 = 0.25
gen2 = 0.5
gen3 = 0.9846
gen4 = 1.969
ocapi = 25/8 # 25GHz / 8 bits per byte
ht31 = 6.4/8 # according to https://en.wikipedia.org/wiki/HyperTransport no AMD processor uses 32 bit HT, only 16 bit. 6.4GT/s per lane, divided by 8 (8 bits per byte) gives [GB/s].

# AMD
# Opteron 6386 SE (Q4'12): according to wikipedia (see link above) only 16 bit HT is used by AMD. this processor has 4 links, but those are uni-directional. Thus 2 bi-directional links (of 16 bits each).
# EPYC: for 2 socket, 64 lanes are sacrificed for infinity fabric, thus 128 lanes total for 2 socket system
amd_n = ["Opteron 6180 SE", "Opteron 6284 SE", "Opteron 6386 SE", "EPYC 7601"]
amd_d = [2010.25, 2012.0, 2013.0, 2017.5]
amd_b = [2*16*ht31, 2*16*ht31, 2*16*ht31, 128*gen3]
amd_m = [42.7, 51.2, 51.2, 2.667*8*8]
plt.plot(amd_d, amd_b, 'ro-', label="AMD", markersize=4)
#for i, txt in enumerate(amd_n):
#  ax.annotate(txt, xy=(amd_d[i],amd_b[i]), xytext=(amd_d[i],amd_b[i]+5), horizontalalignment='right')

# Applied Micro
app_n = ["X-Gene 3"]
app_d = [2017]
app_b = [42*gen3]
app_m = [2.667*8*8] #2667 ddr4 * 8B * 8 channels
app_c = [8] #dram channels
plt.plot(app_d, app_b, 'co-', label="Applied Micro", markersize=4)
#for i, txt in enumerate(app_n):
#  ax.annotate(txt, xy=(app_d[i],app_b[i]), xytext=(app_d[i],app_b[i]+5), horizontalalignment='right')

# Cavium
cav_n = ["ThunderX", "ThunderX2"]
cav_d = [2015]
cav_b = [24*gen3]
cav_m = [2.400*8*4]
plt.plot(cav_d, cav_b, 'mo-', label="Cavium", markersize=4)
#for i, txt in enumerate(cav_n):
#  ax.annotate(txt, xy=(cav_d[i],cav_b[i]), xytext=(cav_d[i],cav_b[i]+5), horizontalalignment='right')

# IBM
ibm_n = ["POWER7", "POWER8", "POWER9"] # POWER7 = Power 750 from slides
ibm_d = [2010.25, 2014.5, 2018]
ibm_b = [30, 48, 48*gen4+48*ocapi]
ibm_m = [28*6.4, 230, 230] #dram bw GB/s # P8 has 410GB/s peak bw see wiki
plt.plot(ibm_d, ibm_b, 'bo-', label="IBM", markersize=4)
#for i, txt in enumerate(ibm_n):
#  ax.annotate(txt, xy=(ibm_d[i],ibm_b[i]), xytext=(ibm_d[i],ibm_b[i]+5), horizontalalignment='right')

# INTEL
intel_n =  ["E5 2690", "E5 2697 v2", "E5 2699 v3", "E5 2699 v4", "Platinum 8180"]
intel_n2 = ["?",       "E7 2890 v2", "E7 4850 v3", "E7 4850 v4", "Platinum 8180"] # different since E7's have more mem bw
intel_d =  [2012.25, 2013.75, 2014.75, 2016.25, 2017.75]
intel_d2 = [2012.25, 2014.25, 2015.50, 2016.50, 2017.75] # TODO: first two data points are fake!
intel_b = [40*gen3, 40*gen3, 40*gen3, 40*gen3, 48*gen3]
intel_m = [85, 85, 85, 85, 2.667*8*6]
plt.plot(intel_d, intel_b, 'go-', label="Intel", markersize=4)
#for i, txt in enumerate(intel_n):
#  ax.annotate(txt, xy=(intel_d[i],intel_b[i]))

# Fujitsu / Oracle
oracle_n = ["SPARC64-XII"]
oracle_d = [2018.125]
oracle_b = [4*8*gen3]
oracle_m = [2.400*8*8]
#plt.plot(oracle_d, oracle_b, 'ko-', label="Fujitsu / Oracle", markersize=4)
#for i, txt in enumerate(oracle_n):
#  ax.annotate(txt, xy=(oracle_d[i],oracle_b[i]), xytext=(oracle_d[i],oracle_b[i]+5), horizontalalignment='right')

# QUALCOMM
qual_n = ["Centriq 2400"]
qual_d = [2018] # second half of 2017
qual_b = [32*gen3]
qual_m = [2.667*8*6]
plt.plot(qual_d, qual_b, 'yo-', label="Qualcomm", markersize=4)
#for i, txt in enumerate(qual_n):
#  ax.annotate(txt, xy=(qual_d[i],qual_b[i]), xytext=(qual_d[i],qual_b[i]+5), horizontalalignment='right')

# Plot setup
plt.axis([2009, 2019, 0, 300])
ax.set_xlabel("Release date")
ax.set_ylabel("Peak aggregate uni-directional interconnect bandwidth [GB/s]")
ax.yaxis.grid(True)
plt.legend(loc=2)

# Output image filename is the name of the script without its extension, plus ".pdf".
filename = os.path.splitext(os.path.basename(__file__))[0] + "-io.pdf"
location = os.path.join(base_path, filename)
plt.savefig(location)

### Fig 2
fig = plt.figure(2)
ax = fig.add_subplot(111)
#width = 0.3 # bar width
#ax2 = ax.twinx()

plt.plot(amd_d, amd_m, 'ro-', label="AMD", markersize=4)
plt.plot(app_d, app_m, 'co-', label="Applied Micro", markersize=4)
#ax2.bar(app_d, app_c, width, color='c')
plt.plot(cav_d, cav_m, 'mo-', label="Cavium", markersize=4)
plt.plot(ibm_d, ibm_m, 'bo-', label="IBM", markersize=4)
plt.plot(intel_d2, intel_m, 'go-', label="Intel", markersize=4)
#plt.plot(oracle_d, oracle_m, 'ko-', label="Fujitsu / Oracle", markersize=4)
plt.plot(qual_d, qual_m, 'yo-', label="Qualcomm", markersize=4)

# Axis setup
ax.set_xlabel("Release date")
ax.set_ylabel("Peak DRAM bandwidth [GB/s]")

# Plot setup
plt.axis([2009, 2019, 0, 300])

#ax.set_ylim(0, 300)
#ax2.set_ylim(1, 10)

ax.yaxis.grid(True)
plt.legend(loc=2)
filename = os.path.splitext(os.path.basename(__file__))[0] + "-dram.pdf"
location = os.path.join(base_path, filename)
plt.savefig(location)

### Fig 3
fig = plt.figure(3)
ax = fig.add_subplot(111)

amd_m = np.array(amd_m, dtype=np.float)
amd_b = np.array(amd_b, dtype=np.float)
amd_r = amd_m/amd_b
plt.plot(amd_d, amd_r, 'ro-', label="AMD")

app_m = np.array(app_m, dtype=np.float)
app_b = np.array(app_b, dtype=np.float)
app_r = app_m/app_b
plt.plot(app_d, app_r, 'co-', label="Applied Micro")

cav_m = np.array(cav_m, dtype=np.float)
cav_b = np.array(cav_b, dtype=np.float)
cav_r = cav_m/cav_b
plt.plot(cav_d, cav_r, 'mo-', label="Cavium")

ibm_m = np.array(ibm_m, dtype=np.float)
ibm_b = np.array(ibm_b, dtype=np.float)
ibm_r = ibm_m/ibm_b # ratio
plt.plot(ibm_d, ibm_r, 'bo-', label="IBM")

# TODO: difficult! e5 and e7 mismatch in year of release.
intel_m = np.array(intel_m, dtype=np.float)
intel_b = np.array(intel_b, dtype=np.float)
intel_r = intel_m/intel_b # ratio
#plt.plot(intel_d2, intel_r, 'go-', label="Intel")

oracle_m = np.array(oracle_m, dtype=np.float)
oracle_b = np.array(oracle_b, dtype=np.float)
oracle_r = oracle_m/oracle_b
#plt.plot(oracle_d, oracle_r, 'ko-', label="Fujitsu / Oracle")

qual_m = np.array(qual_m, dtype=np.float)
qual_b = np.array(qual_b, dtype=np.float)
qual_r = qual_m/qual_b # ratio
plt.plot(qual_d, qual_r, 'yo-', label="Qualcomm")

# Plot setup
plt.axis([2007, 2019, 0, 10])
ax.set_xlabel("Release date")
ax.set_ylabel("DRAM and interconnect bandwidth ratio")
ax.yaxis.grid(True)
plt.legend(loc=2)
filename = os.path.splitext(os.path.basename(__file__))[0] + "-ratio.pdf"
location = os.path.join(base_path, filename)
plt.savefig(location)
