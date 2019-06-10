from setuptools import setup, Extension

setup(name='palindrome',
      version='1.0',
      description='A simple example',
      author='Magnus Lie Hetland',
      py_modules=['hello'],
      ext_modules=[
          Extension('palindrome', ['palindrome2.c', 'palindrome.i'])
      ])
