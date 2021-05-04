# https://github.com/pypa/sampleproject
import pathlib
from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

short_description = 'Friendly Dogecoin JSON-RPC API binding for Python 3'
# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='python-dogecoin',
    version='0.0.2',
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Misha Behersky',
    author_email='bmwant@gmail.com',
    url='https://github.com/bmwant/dogecoin-python',
    keywords='rpc, doge, dogecoin',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
    install_requires=[],  # No extra dependencies
    extras_require={
        'dev': [
            'twine==3.4.1',
            'black==20.8b1',
            'build==0.3.1.post1',
        ],
        'test': ['pytest==6.2.3'],
    },
)
