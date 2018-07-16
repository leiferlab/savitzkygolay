# savitzkygolay
Savitzky-Golay filters loaded from the files produced by Shekhar, *On Simplified Application of Multidimensional Savitzky-Golay Filters and Differentiators*, Progress in Applied Mathematics in Science and Engineering, Bali, Indonesia (2015)

The module depends on numpy, scipy, and opencv. To install opencv
```
python -m pip install opencv-python 
```
appending ```--user``` if you have restricted permission on the machine.

To install, clone the repository and
```
python setup.py install --user
```

The module contains functions to both filter input arrays (in 1, 2, and 3 dimensions) or to just load the kernel in order to use it somewhere else.

Filter data with the function ```filter*D()```, passing ```(input array, size of the kernel, polynomial order, derivative order)```.

Get the filters with the function ```get_*D_filter()```. For the 1D case, the arguments are ```(size, polynomial order, derivative order)```. For the 3-dimensional case, anisotropic size and orders are available. In that case, the parameters ```size``` and ```polynomial order``` are repeated for N times in the function.

To keep the repository lightweight, only a few 3D filters are provided (there is a reasonable collection of 1D and 2D filters, instead). If you need additional ones, ask Francesco. 
