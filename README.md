# savitzkygolay
Savitzky-Golay filters loaded from the files produced by Shekhar, Progress in Applied Mathematics in Science and Engineering, Bali, Indonesia (2015)

To install, clone the repository and
```
python setup.py install --user
```

Get the derivatives with the function ```get_*D_derivative()```. For the 1D case, the arguments are ```(size, polynomial order, derivative order)```. For the N-dimensional case, ```size``` and ```polynomial order``` are repeated for N times.

To keep the repository lightweight, only a few filters are provided (all the 1D and 3D filters together are 150 MB). If you need additional ones, ask Francesco. 
