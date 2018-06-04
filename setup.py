from setuptools import setup, find_packages

with open('protozmq/VERSION', 'r') as f:
    __version__ = f.read().strip()


setup(
    name='protozmq',
    version=__version__,
    description='',
    url='https://github.com/cta-sst-1m/protozmq',
    author='Etienne Lyard, Dominik Neise',
    author_email='neised@phys.ethz.ch',
    packages=find_packages(),
    # tests_require=['pytest>=3.0.0'],
    # setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
        'protobuf',
        'zmq',
    ],
    zip_safe=False,
)
