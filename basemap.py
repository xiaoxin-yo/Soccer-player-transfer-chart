from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

fig = plt.figure(1)
# create Basemap instance for Robinson projection.
m = Basemap(llcrnrlon=-175,llcrnrlat=-80,urcrnrlon=185,urcrnrlat=80,projection='mill')
# draw costlines and coutries
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.5)
m.fillcontinents(color='0.8')

# convert lon and lat to map coordinates
x,y = m(0, 0)

# draw a point
point = plt.text(x,y,'Name', fontsize=20)
point2 = plt.text(x,y,'Name2', fontsize=20)

# this is called every frame
def init():
    point.set_fontsize(0)
    point2.set_fontsize(0)
    return point,point2

start_lon = -20.
start_lat = 35.
end_lon = 60.
end_lat = 60.

# get slope
slope = (end_lat - start_lat) / (end_lon - start_lon)

# animation function.  This is called sequentially
def animate(i):
    x, y = m(i*1 + start_lon, (i*1) * slope + start_lat)
    point.set_fontsize(12)
    point.set_position([x, y])
    point2.set_fontsize(12)
    x2, y2 = m(i+10, i+10)
    point2.set_position([x2,y2])
    return point,point2

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               frames=int(abs(end_lon-start_lon)), interval=1, blit=True, repeat=False)

plt.show()
