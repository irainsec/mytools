from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("VAPT_Altisec.py")
)
