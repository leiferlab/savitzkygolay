import numpy as np
import pkg_resources

def get_1D_filter():
    return 0

def get_3D_filter():
    return 0

def get_1D_derivative(mu, poly, order):
    '''Loads the Savitzky Golay filter of size mu with poly-th polynomial order
    and dimensionality d.'''
    
    folder = pkg_resources.resource_filename('savitzkygolay', 'filters/')
    
    f = open(folder+'1DSavitzkyGolayFilters/CC_00'+str(mu)+'_00'+str(poly)+'.dat',\
            'r')

    #Go through file
    while 1:
        s = f.readline()
        if s=='# Matrix starts:\n':
            break
            
    #Jump to coefficient you want to calculate
    C = np.zeros((mu))
    L = order #order-th derivative
    for l in np.arange(L):
        f.readline()
        
    s = f.readline()
    s = s.split('\t')
    symmetry = s[1]
    s = np.array(s[2:]).astype(np.float)

    #Populate second half based on symmetry (centred filters, leave central 
    #col out)
    if symmetry =='S':
        s = np.append(s,s[0:-1][::-1])
    elif symmetry == 'A':
        s = np.append(s,-1.0*s[0:-1][::-1])
    C = s
    f.close()
    
    return C
        
def get_3D_derivative(mu, nu, rho, polyx, polyy, polyz, order):

    folder = pkg_resources.resource_filename('savitzkygolay', 'filters/')

    f = open('3DSavitzkyGolayFilters/CC_00'+str(mu)+'x00'+str(nu)+'x00'+ \
        str(rho)+'_00'+str(polyx)+'x00'+str(polyy)+'x00'+str(polyz)+'.dat','r')
        
    #Go through file
    while 1:
        s = f.readline()
        if s=='# Matrix starts:\n':
            break
            
    #Jump to coefficient you want to calculate
    #k+j*nu+i*nu*rho with k,j,i=200,020,002
    l0 = 2
    l1 = 2*nu
    l2 = 2*nu*rho

    L = [l0,l1,l2]
    q = len(L)
    C = np.zeros((q,mu*nu*rho))
    p = 0
    S = f.readlines()
    for l in L:
        s = S[l]
        s = s.split('\t')
        symmetry = s[1]
        s = np.array(s[2:]).astype(np.float)

        #Populate second half based on symmetry (centred filters, leave central 
        #col out)
        if symmetry =='S':
            s = np.append(s,s[0:-1][::-1])
        elif symmetry == 'A':
            s = np.append(s,-1.0*s[0:-1][::-1])
        C[p] = s
        p += 1
    f.close()
        
    return C
