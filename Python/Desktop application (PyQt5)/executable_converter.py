import sys
from cx_Freeze import setup, Executable

build_options = {'packages': [], 'excludes': []}
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('CalcTodoTime.py', base=base) #write base python file name here
]

setup(name='my_app',
      version='0.1',
      description='My First App',
      options={'build_exe': build_options},
      executables=executables)


#python setup.py build