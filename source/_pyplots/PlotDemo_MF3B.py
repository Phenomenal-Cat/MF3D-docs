#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:28:49 2020

@author: Aidan Murphy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import cool
#from sklearn import linear_model
#from sklearn.metrics import mean_squared_error, r2_score


# Read MF3D demographic data from spreadsheet
CSVFile = 'MF3B_Demographics.csv'
Data = np.genfromtxt(CSVFile , delimiter=',', dtype=None, encoding=None)
NumData = np.genfromtxt(CSVFile , delimiter=',')
ages = NumData[1:,2] + NumData[1:,3]/12
weights = NumData[1:,4]
sexes = Data[1:,1]
Females = np.where(sexes == 'F')
Males = np.where(sexes == 'M')
SexColors = ((1,0,0),(0,0,1))

#====== Create linear regression object
ageReg = np.linspace(3, 25, 22)
m, b = np.polyfit(ages[Males], weights[Males], 1)   # m = slope, b=intercept
male_pred = m*ageReg + b
m, b = np.polyfit(ages[Females], weights[Females], 1)   # m = slope, b=intercept
fem_pred = m*ageReg + b

#===== Plot demographic data in scatter and histogram plots

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.02
rect_scatter = [left, bottom, width, height]
ScatterLims = [0, 30, 0, 24]
binwidth = 0.5
barcolor = (0.5,0.5,1)

fig = plt.figure(figsize=(8, 8))
gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)

#==== Plot main scatter plot
ax_scatter = fig.add_subplot(gs[1, 0])
ax_scatter.tick_params(direction='in', top=True, right=True)
ax_scatter.plot(ages[Males], weights[Males], c=SexColors[1], marker='o', linestyle='', label='Male', alpha=0.8)
ax_scatter.plot(ages[Females], weights[Females], c=SexColors[0], marker='d', linestyle='', label='Female', alpha=0.8)
ax_scatter.plot(ageReg, male_pred, c=SexColors[1], linewidth=2)
ax_scatter.plot(ageReg, fem_pred, c=SexColors[0], linewidth=2)
plt.axis(ScatterLims)
ax_scatter.set_aspect('auto')
ax_scatter.imshow([[0.5, 0],[1,0.5]], interpolation='bicubic', cmap=cool,
             vmin=0, vmax=1, aspect='auto',
             extent=(ax_scatter.get_xlim()[0], ax_scatter.get_xlim()[1],
                    ax_scatter.get_ylim()[0], ax_scatter.get_ylim()[1]),
             alpha=0.2)
             
ax_scatter.tick_params(axis='both', which='major', labelsize=12, direction='out', top=False, right=False)
#plt.box(on=None)
plt.grid()
plt.legend(numpoints=1, fontsize=12)
plt.xlabel('Age (years)', fontsize=16)
plt.ylabel('Weight (kg)', fontsize=16)

#==== Histogram plots
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax_scatter)
plt.title('MF3B Demographic Summary (N = %d)' % len(ages))
ax_histx.set_facecolor((0.9,0.9,0.9))
#plt.axis('off')
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax_scatter)
ax_histy.set_facecolor((0.9,0.9,0.9))
#plt.axis('off')
ax_histx.tick_params(direction='in', labelbottom=False, labelleft=False, left=False)
ax_histy.tick_params(direction='in', labelleft=False, labelbottom=False, bottom=False)
xbins = np.arange(ScatterLims[0], ScatterLims[1], binwidth)
ybins = np.arange(ScatterLims[2], ScatterLims[3], binwidth)
ax_histx.hist(ages, bins=xbins, color =barcolor, lw=0)
ax_histy.hist(weights, bins=ybins, orientation='horizontal', color =barcolor, lw=0)
ax_histx.set_xlim(ax_scatter.get_xlim())
ax_histy.set_ylim(ax_scatter.get_ylim())

plt.savefig("MF3B_DemographicsPlot.svg")
plt.show()