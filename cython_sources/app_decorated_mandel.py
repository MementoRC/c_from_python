# distutils: language = c++

import cython


# Little help from the .pxd and override of C-functions by inline C and Pure Python calls
# (depending on compiled state)
@cython.exceptval(check=False)
@cython.cfunc
@cython.inline
@cython.returns(cython.double)
def _norm(z: cython.complex):
    if cython.compiled:
        return _std_norm(z)+0
    else:
        return z.real * z.real + z.imag * z.imag


@cython.cfunc
@cython.inline
@cython.returns(cython.complex)
def _complex_number(x: cython.double, y: cython.double):
    if cython.compiled:
        return _std_complex_number(x, y)
    else:
        return complex(x, y)


@cython.exceptval(check=False)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.ccall
@cython.locals(i=cython.int)
@cython.returns(cython.int)
def app_decorated_mandel(x: cython.double,
                         y: cython.double,
                         max_iters: cython.int,
                         value: cython.p_uchar
                         ):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c: cython.complex = _complex_number(x, y)
    z: cython.complex = _complex_number(0, 0)
    _4: cython.double = 4
    for i in range(max_iters):
        z = z * z + c
        if _norm(z) >= _4:
            value[0] = i
            return 0
    value[0] = max_iters
    return max_iters
