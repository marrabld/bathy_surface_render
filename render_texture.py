from osgeo import gdal
import scipy.misc
import sys
import os
import pylab
import numpy as np

texture = np.ones((3475, 3560, 3), dtype=np.uint8)

folder_data = './data/'
file_data = 'liz_2009_qb.tif'
gtif = gdal.Open(os.path.join(folder_data, file_data))

band_num = 3

#for i_band in reversed(list(range(1, band_num+1))):
for i_band in range(1, band_num + 1):
    print(i_band)
    try:
        srcband = gtif.GetRasterBand(band_num)
    except RuntimeError as e:
        # for example, try GetRasterBand(10)
        print('Band ( %i ) not found' % band_num)
        print(e)
        sys.exit(1)

    texture[:, :, i_band - 1] = srcband.ReadAsArray()



# pylab.imshow(texture[:, :, 0])
# pylab.show()
# pylab.imshow(texture[:, :, 1])
# pylab.show()
# pylab.imshow(texture[:, :, 2])
# pylab.show()
pylab.imshow(texture)
pylab.show()

#pylab.imsave('./data/texture_1.jpg', texture)
pylab.imsave()