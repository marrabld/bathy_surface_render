# coding: utf-8

# In[1]:



import os
from osgeo import gdal
from tvtk.api import tvtk
from mayavi import mlab
from PIL import Image

from scipy.ndimage.filters import median_filter
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.filters import convolve

SCALE = True
TEXTURE = False #True



folder_data = './data/'
#file_data = 'lizard_bathy.tif'
file_data = 'ccmr_south_2015_09_22_bathy_12345_pair6_30m_10M_alut_unc.tif'
gtif = gdal.Open(os.path.join(folder_data, file_data))

try:
    srcband = gtif.GetRasterBand(1)
except RuntimeError as e:
    # for example, try GetRasterBand(10)
    print('Band ( %i ) not found' % band_num)
    print(e)
    sys.exit(1)

# In[5]:
b = srcband.ReadAsArray()

if SCALE:
    b[b == -998.0] = 0.0
    b[b == -999.0] = 30.0
    b *= -1

    # Filter the image

b = median_filter(b, 5)
#b = gaussian_filter(b, 2)
#b = convolve(b, (4, 4))

if TEXTURE:
    im1 = Image.open("./data/texture.jpg")
    im2 = im1.rotate(90)
    im2.save("./data/texture_90.jpg")
    bmp1 = tvtk.JPEGReader()
    bmp1.file_name = "./data/texture_90.jpg"  # any jpeg file

    my_texture = tvtk.Texture(input_connection=bmp1.output_port, interpolate=0)


mlab.figure(size=(640, 800), bgcolor=(0.16, 0.28, 0.46))

surf = mlab.surf(b, color=(1, 1, 1), warp_scale=8)

if TEXTURE:
    surf.actor.enable_texture = True
    surf.actor.tcoord_generator_mode = 'plane'
    surf.actor.actor.texture = my_texture

mlab.view(distance=100)
mlab.show()
