from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"
from parseExampleXML import exampleXML
import pdb
import math

fig = plt.figure(1)
# create Basemap instance for Robinson projection.
m = Basemap(llcrnrlon=-175,llcrnrlat=-80,urcrnrlon=185,urcrnrlat=80,projection='mill')
# draw costlines and coutries
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.5)
m.fillcontinents(color='0.8')

# convert lon and lat to map coordinates
x,y = m(0, 0)

# read in XML
array = exampleXML()

# draw a point
points = []
for i in array:
    points.append(plt.text(x,y,str(i[0]), fontsize=20))

# this is called every frame
def init():
    for i in points:
        i.set_fontsize(0)
    return tuple(points)

# calculate slopes
slopes = []
for i in array:
    slopes.append((i[2][0] - i[1][0]) / (i[2][1] - i[1][1]))

# calculate distance
scales = []
for i in array:
    scales.append(math.sqrt((i[2][0] - i[1][0])**2 + (i[2][1] - i[1][1])**2)/500)

# animation function.  This is called sequentially

def animate(i):
    stop = False
    for index in range(len(array)):
        if array[index][2][0] > array[index][1][0] and array[index][2][1] > array[index][1][1]:
            new_lat = scales[index]*i * abs(slopes[index]) + array[index][1][0]
            new_lon = scales[index]*i + array[index][1][1] 
            x, y = m(new_lon, new_lat)
            if new_lat == array[index][2][0] and new_lon == array[index][2][1]:
                stop = True
        elif array[index][2][0] > array[index][1][0] and array[index][2][1] < array[index][1][1]:
            new_lat = scales[index]*i * abs(slopes[index]) + array[index][1][0]
            new_lon = scales[index]*-1*i + array[index][1][1]
            x, y = m(new_lon, new_lat)
            if new_lat == array[index][2][0] and new_lon == array[index][2][1]:
                stop = True
        elif array[index][2][0] < array[index][1][0] and array[index][2][1] > array[index][1][1]:
            new_lat = scales[index]*-1*i * abs(slopes[index]) + array[index][1][0]
            new_lon = scales[index]*i + array[index][1][1]
            x, y = m(new_lon, new_lat)
            if new_lat == array[index][2][0] and new_lon == array[index][2][1]:
                stop = True
        else:
            new_lat = scales[index]*-1 * i * abs(slopes[index]) + array[index][1][0]
            new_lon = scales[index]*-1 * i + array[index][1][1]
            x, y = m(new_lon, new_lat)
            if new_lat == array[index][2][0] and new_lon == array[index][2][1]:
                stop = True
        if stop:
            points[index].set_fontsize(0)
        else:
            points[index].set_fontsize(12)
            points[index].set_position([x, y])

    return tuple(points)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               frames=500, interval=1, blit=True, repeat=False)

plt.show()
