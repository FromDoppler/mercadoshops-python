import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='mercadoshops-python',
      version='0.1.0',
      description='API wrapper for MercadoShops Graph written in Python',
      long_description=read('README.md'),
      url='https://github.com/FromDoppler/mercadoshops-python',
      author='Fromdoppler',
      author_email='integrations@fromdoppler.com',
      license='GPL',
      packages=['mercadoshops'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
