from distutils.errors import LibError
from setuptools import setup, find_packages

classifers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operation System :: Microsoft :: Windows :: Windows 10',   
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'       
]

setup(
    name='albertpamonag',
    version='0.0.1',
    description='testing',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Albert Pamonag',
    author_email='albertpamonag@gmail.com',
    license='MIT',
    classifiers=classifers
    keywords='concrete',
    packages= find_packages()
)