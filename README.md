# savitzkygolay
Savitzky-Golay filters loaded from the files produced by Shekhar, Progress in Applied Mathematics in Science and Engineering, Bali, Indonesia (2015)

To install, clone the repository and
```
python setup.py install --user
```

Get the filter with the function ```get_filter(size, polynomial order, derivative order, dimensionality)```. To keep the repository lightweight, only a few filters are provided (all the 1D and 3D filters together are 150 MB). If you need additional ones, ask Francesco. 
