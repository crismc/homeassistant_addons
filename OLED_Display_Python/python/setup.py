import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'pioled',
      version           = '0.1',
      author            = 'Chris Churchill',
      author_email      = 'chris@serva.co.uk',
      description       = 'Python library python script for I2C SSD1306-based 128x32 pixel OLED displays with a Raspberry Pi.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'http://192.168.0.2:3000/personal/oled_ssd1306',
      install_requires  = [],
      packages          = find_packages())
