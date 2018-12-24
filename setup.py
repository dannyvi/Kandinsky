from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
ext_modules = [
    Extension("colorconvertc",
              ["colorconvertc.pyx"],
              libraries=["m"],
              include_dirs=[np.get_include()]
          )
]
setup(
    #ext_modules = cythonize("glcprocedure.pyx")
    name = "colorconvertc",
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules
)
