# distutils: language = c++

cdef extern from "<complex.h>" namespace "std" :
    cdef double _std_norm "abs" (complex z) nogil

cdef inline complex _std_complex_number(double x, double y):
    return x + y * 1j

#cdef inline double _std_norm(double complex z):
#    return z.real * z.real + z.imag * z.imag
