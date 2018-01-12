
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii


def makeHist(x, y):
    # Estimate the 2D histogram
    nbins = 10
    H, xedges, yedges = np.histogram2d(x, y, bins=nbins)
    # H needs to be rotated and flipped
    H = np.rot90(H)
    H = np.flipud(H)
    # Mask pixels with a value of zero
    Hmasked = np.ma.masked_where(H == 0, H)
    plt.pcolormesh(xedges, yedges, Hmasked)  #, vmin=0, vmax=150)
    plt.colorbar()


# xy density histograms of DAOMASTER's .mag matched filter files.
ufilt = ascii.read('ufilter.mag')
xu, yu = ufilt['col2'], ufilt['col3']
bfilt = ascii.read('bfilter.mag')
xb, yb = bfilt['col2'], bfilt['col3']
vfilt = ascii.read('vfilter.mag')
xv, yv = vfilt['col2'], vfilt['col3']
ifilt = ascii.read('daom.raw')
xi, yi = ifilt['col2'], ifilt['col3']

plt.subplot(221)
plt.title("Filter U")
# makeHist(xu, yu)
plt.scatter(xu, yu, s=4)
plt.subplot(222)
plt.title("Filter B")
# makeHist(xb, yb)
plt.scatter(xb, yb, s=4)
plt.subplot(223)
plt.title("Filter V")
# makeHist(xv, yv)
plt.scatter(xv, yv, s=4)
plt.subplot(224)
plt.title("DAOM raw")
# makeHist(xi, yi)
plt.scatter(xi, yi, s=4)
plt.show()
