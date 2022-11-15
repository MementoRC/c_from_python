import setuptools
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
#import numpy
#import pandas

cython_sources = ["cython_sources/*_mandel*.py"]
cython_kwargs = {
  "language_level": 3,
  "annotate": True,
}

setup(ext_modules=(cythonize(cython_sources, **cython_kwargs)),
      requires=['Cython'])
