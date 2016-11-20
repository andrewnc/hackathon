import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = 0*x

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ylim([-100,1000])
plt.xlim([-100,1000])
ax.text(0.5, 0.5, 'U',fontsize=400)

coords = []

def x_of_t(p1,p2,p3,p4,t):
    return p1[0]*(1-t)**3 + 3*p2[0]*(1-t)**2*t+3*p3[0]*(1-t)*(t**2)+p4[0]*t**3

def y_of_t(p1,p2,p3,p4,t):
    return p1[1]*(1-t)**3 + 3*p2[1]*(1-t)**2*t+3*p3[1]*(1-t)*(t**2)+p4[1]*t**3

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print 'x = %d, y = %d'%(
        ix, iy)

    global coords
    coords.append((ix, iy))

    if len(coords) == 1000:
        fig.canvas.mpl_disconnect(cid)
        plt.close()

    return coords


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()


print coords

# t = np.linspace(0,1,1000)
# plt.plot(x_of_t(coords[0],coords[1],coords[2],coords[3],t),y_of_t(coords[0],coords[1],coords[2],coords[3],t))
# plt.show()