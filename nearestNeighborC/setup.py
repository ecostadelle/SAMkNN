 
from distutils.core import setup, Extension

module1 = Extension('libNNPythonIntf',
                    include_dirs = ['/usr/include/python2.7', '/usr/include/python2.7/numpy'],
                    libraries = [],
                    library_dirs = [],
		    extra_compile_args = ['-O3'],
                    sources = ['intf.cpp'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       author = 'Martin v. Loewis',
       author_email = 'martin@v.loewis.de',
       url = 'http://docs.python.org/extending/building',
       long_description = '''This is really just a demo package.''',
       ext_modules = [module1])
