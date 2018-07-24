from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

#Get project's long description
long_desc = """\ Python package to help developers easily access DHL Worldwide express service from their python applications.
The package creates SOAP requests using the zeep package(https://pypi.org/project/zeep/)
to request shipping rates, create shipments and schedule pick ups.
Built around an initial python dhl package by Benjamin Polovic (https://github.com/benqo/python-dhl)
"""

setup(
     name='soapdhl',
     version='1.0',
     description='Python SOAP client for DHL Express web service',
     long_description = long_desc,

     url = 'https://github.com/Maestro1/soapdhl',

     author='Daniel Karama',
     author_email='danielkarama13@gmail.com',

     license='MIT',

     classifiers=[
       'Development Status :: 1',

       'Intended Audience :: Developers',

       'License :: OSI Approved ::MIT License',

       'Programming Language :: Python :: 3.6'

       ],


       packages =['dhl','dhl/resources'],

       install_requires=['zeep']
         

     ]

	)