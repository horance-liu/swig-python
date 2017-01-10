#File: setup.py
#!/usr/bin/python2.7

from distutils.core import setup, Extension

example_module = Extension('_example',
                        sources=['example_wrap.cxx',
                                 'example.cxx'
                                ],
                      )

setup(name = 'example',
        version = '0.1',
        author = 'horance',
        description = 'swig example',
        ext_modules = [example_module],
        py_modules = ['example'],
    )