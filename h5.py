import cv2
import numpy as np
import h5py
f = h5py.File('keras_model.h5', 'r')
dset = f['mask']
data = np.array(dset[:,:,:])
file = 'test1.jpg'
cv2.imwrite(file, data)