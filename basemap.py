import pylab

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# # making location list
# lats = []
# for i in range(len(args[1])):
#     lats.append(i*(180./float(len(args[1])))-90)
# lons = []
# for i in range(len(args[1][0])):
#     lons.append(i*(360./float(len(args[1][0])-1))-180)

fig = plt.figure(1)
# create Basemap instance for Robinson projection.
m = Basemap(llcrnrlon=-20.,llcrnrlat=35.,urcrnrlon=60.,urcrnrlat=60.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            area_thresh=10000000.
            )#lat_0=40.,lon_0=20.,)
# draw costlines and coutries
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.5)
m.fillcontinents(color='0.8')
# # compute the lons and lats to fit the projection
# x, y = m(*np.meshgrid(lons, lats))
## draw filled contours.
#f1 = m.contourf(x,y,args[1],40,cmap=colorbar,vmin=kwargs.get('low',-10),vmax=kwargs.get('high',10))

pylab.show()
