from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

setup(name='nms',
        ext_modules=[CUDAExtension('nms', ['nms.cpp', 'nms_kernel.cu'])],
        cmdclass={'build_ext': BuildExtension})

