from distutils.core import setup
setup(name='chilispendfrom',
      version='1.0',
      description='Command-line utility for chilicoin "coin control"',
      author='Gavin Andresen',
      author_email='gavin@chilicoinfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
