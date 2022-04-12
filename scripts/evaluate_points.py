import os
import glob
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#data_folder = '02691156'
data_folder = 'simple_table'


basedir = os.path.abspath(os.path.dirname(__file__+'../../../'))
data_dir = os.path.abspath(os.path.join(basedir, '..', 'data', 'train_data', data_folder))
print('Dirname:', data_dir)

## 3D Points ##
points_dir = os.path.join(data_dir, '4_points')
pointcloud_dir = os.path.join(data_dir, '4_pointcloud')


points_files = glob.glob(points_dir+'/*.npz')
for f in points_files:
    data = np.load(f)
    ## points and occupancies ##
    x = data['points']
    occ = data['occupancies']
    occ = occ*1.
    idxs = np.where(occ == 1.)

    print('data', x.shape)
    print('occ', occ.shape)


    ## visualize points ##
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[idxs, 0], x[idxs, 1], x[idxs,2])
    plt.show()






