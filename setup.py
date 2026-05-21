# setup.py
from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy as np

setup(
    name="SpectralEntropy",
    version="1.0.0",
    packages=find_packages(exclude=["*tests*"]),
    python_requires=">=3.7",
    ext_modules=cythonize(
        "spectral_entropy/tools_fast.pyx",
        annotate=False,
        compiler_directives={
            'language_level': "3",
            'cdivision': True,
            'boundscheck': False,
            'wraparound': False,
        },
    ),
    include_dirs=[np.get_include()],
    zip_safe=False,
)
