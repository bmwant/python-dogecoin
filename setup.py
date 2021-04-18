# https://github.com/pypa/sampleproject
from setuptools import setup, find_packages


LONG_DESCRIPTION = """
This package allows performing commands such as listing the current balance
and sending coins to the Satoshi (original) client from Python. The communication with the
client happens over JSON-RPC.
"""

setup(
    name='python-dogecoin',
    version='0.0.1',
    description='Friendly Dogecoin JSON-RPC API binding for Python',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/bmwant/dogecoin-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'}
)
