"""-----------------------------------------------------------------------------
Completer la fonction PeakDetect declaree ci-dessous,
s'inspirer du source disponible au lien suivant (fonction "peakdetect") :
   https://gist.github.com/sixtenbe/1178136
-----------------------------------------------------------------------------"""

#-------------------------------------------------------------------------------
def PeakDetect(Values, Delta):
   return []
#-------------------------------------------------------------------------------

import os; os.system('cls')
import matplotlib.pyplot as plt

#Defining the x and y arrays
y = [0, 0, 0, 0.5, 0, 0.8, 0, 0, 2, 6, 8, 7.5, 7, 5, 2, 1, 0, 0, 0.5, 0, 0, 0,
4, 5, 4.5, 2, 0, 0, 0, 0.5, 0, 0, 10.2, 15, 20.3, 20.1, 20, 12, 8, 6, 5, 5.5,
8, 10, 10.1, 10, 8.3, 4.2, 2, 1, 0, 0, 4, 6, 2, 0, 0, 0.1, 0, 0, 0.5, 0, 0, 0,
10, 14.5, 15, 14.8, 14.9, 14, 8, 7,5, 8.2, 14.8, 14.5, 6, 1, 2, 1, 0.5, 0.2, 0]

x = range(len(y))

#Find peaks
peak_pos    : int   = []
peak_height : float = []

peak_pos = PeakDetect(Values = y, Delta = 2)
for item in peak_pos:
   peak_height.append(y[item])

#Plotting
fig = plt.figure("Plotting peak detection")
ax  = fig.subplots()

ax.plot(x,y)
ax.scatter(peak_pos, peak_height, color = 'r', s = 50, marker = 'D', label = 'Peaks')
ax.legend()
ax.grid()

plt.show()
