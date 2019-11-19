import os
libs= {'pillow','request',\
      'beautifulsoup4','wheel','networkx','sympy'\
      'pyinstaller','django','flask','werobot','pyqt5',\
      'pyopengl','pypdf2','docopt','pygame'}
try:
    for lib in libs:
        os.system('pip install '+lib)
    print('Successful')
except:
    print('Failed Somehow')