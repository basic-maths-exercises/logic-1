import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("mydata.dat")

filter = np.zeros( len(data) )
for i in range(len(data)) :
  if data[i] == 5 : filter[i] = 1 
  
xvals = np.linspace( 0, len(data), len(data), endpoint=False )
plt.plot( xvals, filter, 'ko' )
plt.savefig("data.png")
