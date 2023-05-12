import numpy as np
import pkg_resources
import cv2
from scipy.ndimage.filters import convolve as spconvolve

def filter1D(A, mu, poly, order=0):
    '''
    Filters a 1D array using the specified Savitzky-Golay filter.
    
    Parameters
    ----------
    A: numpy array
        Input 1D array to be filtered.
    mu: int
        Size of the mu kernel.
    poly: int
        Order of the best-fit polynomial to be used.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    B:
        A numpy array containing the filtered input array. B has the same size
        as A. Boundary effects are not cut out.
    '''
    
    C = get_1D_filter(mu,poly,order)
    B = np.convolve(A,C,mode='full')
    
    return B

def filter2D(A, mu, poly, order=0):
    '''
    Filters a 2D array using the specified Savitzky-Golay filter.
    
    Parameters
    ----------
    A: numpy array
        Input 2D array (image) to be filtered. The function accepts stacks of
        images with shapes (x,y,z). If a stack of images is passed, the 
        filtering will take place only in the (x,y) planes separately.
    mu: int
        Size of the mu*mu kernel.
    poly: int
        Order of the best-fit polynomial to be used.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    B:
        A numpy array containing the filtered input array. B has the same size
        as A.
    '''
    
    C = get_2D_filter(mu,poly,order)
    B = cv2.filter2D(src=A,ddepth=-1,kernel=C)
    
    return B
    
def filter3D(A, mu, poly, order=0):
    '''
    Filters a 3D array using the specified Savitzky-Golay filter.
    
    Parameters
    ----------
    A: numpy array
        Input 3D array to be filtered.
    mu: int
        Size of the mu*mu*mu kernel. To use anisotropic orders the function 
        get_3D_filter() and convolve separately.
    poly: int
        Order of the best-fit polynomial to be used. To use anisotropic orders
        use the function get_3D_filter() and convolve separately.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    B:
        A numpy array containing the filtered input array. B has the same size
        as A.
    '''
    
    C = get_3D_filter(mu, mu, mu, poly, poly, poly, order)
    C = C[0]
    B = spconvolve(A,C)
    
    return B
    
def get_1D_filter(mu,poly,order=0):
    '''
    Loads the 1D Savitzky-Golay filter of size mu with poly-th polynomial 
    order.
    
    Parameters
    ----------
    mu: int
        Size of the mu kernel.
    poly: int
        Order of the best-fit polynomial to be used.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    C:
        A numpy array of shape (mu) containing the desired filter.
    '''
    
    #Get the path of the folder containing the filters inside the module folder.
    folder = pkg_resources.resource_filename('savitzkygolay', 'filters/')
    
    #Open file
    f = open(folder+'1DSavitzkyGolayFilters/CC_'+str(mu).zfill(3)+
            '_'+str(poly).zfill(3)+'.dat',
            'r')

    #Go through file
    while 1:
        s = f.readline()
        if s=='# Matrix starts:\n':
            break
            
    #Skip lines until you're at the right order. 
    for o in np.arange(order):
        f.readline()
        
    s = f.readline()
    s = s.split('\t')
    symmetry = s[1]
    s = np.array(s[2:]).astype(float)

    #Populate second half based on symmetry (centred filters, leave central 
    #col out)
    if symmetry =='S':
        s = np.append(s,s[0:-1][::-1])
    elif symmetry == 'A':
        s = np.append(s,-1.0*s[0:-1][::-1])
    C = s
    f.close()
    
    return C
    
def get_2D_filter(mu, poly, order=0):
    '''
    Loads the 2D Savitzky-Golay filter of size mu with poly-th polynomial 
    order.
    
    Parameters
    ----------
    mu: int
        Size of the mu*mu kernel.
    poly: int
        Order of the best-fit polynomial to be used.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    C:
        A numpy array of shape (mu, mu) containing the desired filter.
    '''
    
    #Get the path of the folder containing the filters inside the module folder.
    folder = pkg_resources.resource_filename('savitzkygolay', 'filters/')
    
    smu = str(mu).zfill(3)
    spoly = str(poly).zfill(3)
    
    #Open file
    f = open(folder+'2DSavitzkyGolayFilters/CC_'+smu+'x'+smu+\
            '_'+spoly+'x'+spoly+'.dat',
            'r')
    
    #Go through file
    while 1:
        s = f.readline()
        if s=='# Matrix starts:\n':
            break
    
    #Skip lines until you're at the right order. 
    for o in np.arange(order):
        f.readline()
              
    s = f.readline()
    s = s.split('\t')
    f.close()
    
    #Find out what the symmetry of the line is.
    symmetry = s[1]
    
    #Populate the first half of the filter from the stored numbers.
    s = np.array(s[2:]).astype(float)

    #Populate  thesecond half based on symmetry. These are centred filters, so
    #leave the central column out.
    if symmetry =='S':
        s = np.append(s,s[0:-1][::-1])
    elif symmetry == 'A':
        s = np.append(s,-1.0*s[0:-1][::-1])
    
    C = s.reshape((mu,mu))
    
    return C

def get_3D_filter(mu, nu, rho, polyx, polyy, polyz, order):
    '''
    Loads the 3D Savitzky-Golay filter of size mu with poly-th polynomial 
    order.
    
    Parameters
    ----------
    mu: int
        Size of the kernel along the first dimension.
    nu: int
        Size of the kernel along the second dimension.
    rho: int
        Size of the kernel along the third dimension.
    polyx: int
        Order of the best-fit polynomial to be used along the first dimension.
    polyy: int
        Order of the best-fit polynomial to be used along the second dimension.
    polyz: int
        Order of the best-fit polynomial to be used along the third dimension.
    order: int
        Order of the derivative to be calculated. oder=0 returns the filter to
        calculate the filtered value at the central node of the kernel.
        
    Returns
    -------
    C:
        A numpy array of shape (3, mu, nu, rho) containing the desired filter.
        If order is 0, then pick only C[0,...].
    '''

    folder = pkg_resources.resource_filename('savitzkygolay', 'filters/')

    f = open(folder+'3DSavitzkyGolayFilters/CC_00'+str(mu)+'x00'+str(nu)+'x00'+ \
        str(rho)+'_00'+str(polyx)+'x00'+str(polyy)+'x00'+str(polyz)+'.dat','r')
        
    #Go through file
    while 1:
        s = f.readline()
        if s=='# Matrix starts:\n':
            break
            
    #Jump to coefficient you want to calculate
    #k+j*nu+i*nu*rho with k,j,i=200,020,002
    l0 = order
    l1 = order*nu
    l2 = order*nu*rho

    L = [l0,l1,l2]
    q = len(L)
    C = np.zeros((q,mu*nu*rho))
    p = 0
    S = f.readlines()
    for l in L:
        s = S[l]
        s = s.split('\t')
        symmetry = s[1]
        s = np.array(s[2:]).astype(float)

        #Populate second half based on symmetry (centred filters, leave central 
        #col out)
        if symmetry =='S':
            s = np.append(s,s[0:-1][::-1])
        elif symmetry == 'A':
            s = np.append(s,-1.0*s[0:-1][::-1])
        C[p] = s
        p += 1
    f.close()
        
    return C.reshape((q,mu,nu,rho))
    
def get_1D_derivative(mu=5, poly=3, order=2):
    '''
    Legacy, not to break previous scripts. Just an alias for the actual
    function get_1D_filter().
    '''
    
    return get_1D_filter(mu,poly,order)  
