# Data Generation Environment (Adapted from OccupancyNet)


## Installation
First you have to make sure that you have all dependencies in place.
The simplest way to do so, is to use [anaconda](https://www.anaconda.com/). 

You can create an anaconda environment called `data_generation_env` using
```
conda env create -f environment.yaml
conda activate data_generation_env
```

Then, install the external folders in `external/mesh_fusion`

```
    # build pyfusion
    cd libfusioncpu
    mkdir build
    cd build
    cmake ..
    make
    cd ..
    pip install -e .
    
    cd ..
    # build pyrender
    cd librender
    pip install -e .
    
    cd ..
    # build PyMCubes
    cd libmcubes
    pip install -e .
```

Next, install im2mesh
You can do this via
```
pip install -e .
```

## Dataset

To evaluate a pretrained model or train a new model from scratch, you have to obtain the dataset.
To this end, there are two options:

1.  you can download the ShapeNet dataset and run the preprocessing pipeline yourself

Take in mind that running the preprocessing pipeline yourself requires a substantial amount time and space on your hard drive.
Unless you want to apply our method to a new dataset, we therefore recommmend to use the first option.
Alternatively, you can also preprocess the dataset yourself.
To this end, you have to follow the following steps:
* download the [ShapeNet dataset v1](https://www.shapenet.org/) and put into `data/external/ShapeNet`. 

You are now ready to build the dataset:

## Building the dataset

The repository generates a set of points labeled with the occupancy and the pointcloud.
We first need to generate in config.sh the desired parameters.

```
cd scripts
bash dataset_shapenet/build.sh
``` 

